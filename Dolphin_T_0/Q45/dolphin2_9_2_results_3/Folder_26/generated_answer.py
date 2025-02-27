from itertools import permutations

def palindromes_between_indices(string):
    letters = [c for c in string[4:7] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        for i in range(len(perm) - 2):
            for j in range(i + 2, len(perm) + 1):
                if perm[i:j] == perm[i:j][::-1]:
                    palindromes.add(''.join(perm[i:j]).lower())
    return palindromes