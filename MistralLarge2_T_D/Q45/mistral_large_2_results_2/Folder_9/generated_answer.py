from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = ''.join(filter(str.isalpha, s[:7].lower()))
    palindromes = set()
    for length in range(7, len(substr) + 1):
        for perm in permutations(substr, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes