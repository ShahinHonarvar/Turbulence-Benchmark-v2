from itertools import permutations

def palindromes_between_indices(s):
    unique_letters = set(s[4:7].lower())
    if len(unique_letters) < 3:
        return set()
    all_permutations = []
    for letters in permutations(unique_letters):
        all_permutations.append(''.join(letters))
    palindromes = set()
    for permutation in all_permutations:
        if permutation == permutation[::-1]:
            palindromes.add(permutation)
    return palindromes