from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    subset = [char for char in s[:9] if char.isalpha()]
    length_subset = len(subset)
    palindromes = set()
    for length in range(7, length_subset + 1):
        for perm in permutations(subset, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes