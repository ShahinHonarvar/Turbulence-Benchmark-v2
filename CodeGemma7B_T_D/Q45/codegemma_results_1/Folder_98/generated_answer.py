from itertools import permutations

def palindromes_between_indices(text):
    palindromes = set()
    for perm in permutations(text[3:6]):
        if perm[0].lower() == perm[2].lower():
            palindromes.add(''.join(perm))
    return palindromes