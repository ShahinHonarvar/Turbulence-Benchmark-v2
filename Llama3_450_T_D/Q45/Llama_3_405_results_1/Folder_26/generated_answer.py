from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(_s):
        return _s == _s[::-1]
    letters = [c.lower() for c in s[4:7] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes