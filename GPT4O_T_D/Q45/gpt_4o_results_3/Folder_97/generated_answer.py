from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join((ch.lower() for ch in s[:5] if ch.isalpha()))
    palindromes = set()
    if len(substring) < 3:
        return palindromes
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes