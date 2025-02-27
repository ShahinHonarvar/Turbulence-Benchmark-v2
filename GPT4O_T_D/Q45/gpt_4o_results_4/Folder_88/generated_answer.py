from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substr = s[3:8]
    substr = ''.join(filter(str.isalpha, substr)).lower()
    if len(substr) < 6:
        return set()
    perms = set(permutations(substr))
    palindromes = set()
    for perm in perms:
        candidate = ''.join(perm)
        for i in range(3, len(candidate) - 2):
            for j in range(i + 3, len(candidate) + 1):
                substring = candidate[i:j]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return {p for p in palindromes if len(p) >= 6}