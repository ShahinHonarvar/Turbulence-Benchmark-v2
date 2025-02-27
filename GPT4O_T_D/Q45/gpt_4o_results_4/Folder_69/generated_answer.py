from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[:4]
    english_letters = [char for char in substring if char.isalpha()]
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for size in range(4, len(english_letters) + 1):
        for perm in permutations(english_letters, size):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes