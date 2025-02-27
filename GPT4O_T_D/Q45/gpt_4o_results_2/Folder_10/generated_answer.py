from itertools import permutations

def palindromes_between_indices(s):
    substr = ''.join([c.lower() for c in s[:6] if c.isalpha()])
    perms = set(permutations(substr))
    palindromes = set()
    for perm in perms:
        perm_str = ''.join(perm)
        for length in range(3, len(perm_str) + 1):
            for start in range(len(perm_str) - length + 1):
                sub = perm_str[start:start + length]
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes