from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join([c for c in s[:6] if c.isalpha()])
    substring = substring.lower()
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes