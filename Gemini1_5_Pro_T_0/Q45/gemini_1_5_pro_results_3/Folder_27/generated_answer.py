import itertools
    from collections import Counter

def palindromes_between_indices(string):
    letters = ''.join(filter(str.isalpha, string[2:9])).lower()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(letters, length):
            for permutation in itertools.permutations(combination):
                word = ''.join(permutation)
                if word == word[::-1] and len(word) >= 6:
                    palindromes.add(word)
    return palindromes