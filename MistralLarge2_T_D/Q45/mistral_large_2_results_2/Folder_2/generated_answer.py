from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = ''.join(filter(str.isalpha, s[1:6]))
    subset = subset.lower()
    palindromes = set()
    for length in range(6, len(subset) + 1):
        for perm in permutations(subset, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes