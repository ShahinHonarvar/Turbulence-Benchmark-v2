from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = ''.join(filter(str.isalpha, s[2:9])).lower()
    unique_letters = set(subset)
    all_permutations = set()
    for length in range(4, len(subset) + 1):
        for perm in permutations(unique_letters, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                all_permutations.add(candidate)
    return all_permutations