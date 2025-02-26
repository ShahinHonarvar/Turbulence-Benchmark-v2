from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:8] if char.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for perm in set(permutations(letters, 6)):
        for i in range(6):
            candidate = list(perm)
            candidate[5 - i] = perm[i]
            candidate_str = ''.join(candidate)
            if candidate_str == candidate_str[::-1]:
                palindromes.add(candidate_str)
    return palindromes