from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[3:9].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for length in range(4, len(letters) + 1):
        for p in permutations(letters, length):
            p_str = ''.join(p)
            if is_palindrome(p_str):
                palindromes.add(p_str)
    return palindromes