from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:8]
    valid_letters = [char.lower() for char in letters if char.isalpha()]
    if len(valid_letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(valid_letters)):
        for i in range(len(perm)):
            for j in range(i + 3, len(perm) + 1):
                candidate = ''.join(perm[i:j] + perm[i:j][::-1])
                if len(candidate) >= 3 and candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes