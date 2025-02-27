from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[3:6].lower()
    letters = Counter((c for c in substring if c.isalpha()))
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            palindrome = ''.join(perm)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes