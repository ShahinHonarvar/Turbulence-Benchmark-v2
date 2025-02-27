from itertools import permutations

def palindromes_between_indices(text):
    letters = [char for char in text[4:10] if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for permutation in permutations(letters, r):
            candidate = ''.join(permutation).lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes