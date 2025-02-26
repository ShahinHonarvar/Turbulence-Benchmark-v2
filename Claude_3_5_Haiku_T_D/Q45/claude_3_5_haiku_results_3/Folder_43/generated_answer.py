from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    letters = s[2:6]
    alpha_letters = [char.lower() for char in letters if char.isalpha()]
    if len(alpha_letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(alpha_letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            mirror = candidate[::-1]
            if len(candidate) >= 4:
                for j in range(len(candidate) - 3):
                    test_perm = candidate[j:j + len(candidate) // 2] + mirror[j:j + len(candidate) // 2]
                    if test_perm == test_perm[::-1] and len(test_perm) >= 4:
                        palindromes.add(''.join(test_perm))
    return palindromes