import itertools

def palindromes_between_indices(s):
    palindromes = set()
    for length in range(6, len(s) + 1):
        for combination in itertools.permutations(s, length):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes