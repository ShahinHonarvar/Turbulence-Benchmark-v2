import itertools

def palindromes_between_indices(text):
    letters = sorted([char for char in text[1:9] if char.isalpha()])
    palindromes = set()
    for r in range(7, 9):
        for permutation in itertools.permutations(letters, r):
            if ''.join(permutation) == ''.join(permutation)[::-1]:
                palindromes.add(''.join(permutation).lower())
    return palindromes