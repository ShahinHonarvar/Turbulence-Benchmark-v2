from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[1:4] if c.isalpha()]
    palindromes = set()
    if len(chars) < 2:
        return palindromes
    unique_permutations = set(permutations(chars, len(chars)))
    for perm in unique_permutations:
        perm_str = ''.join(perm)
        if len(perm_str) >= 4:
            for i in range(len(perm_str) - 3):
                for j in range(i + 4, len(perm_str) + 1):
                    sub_perm = perm_str[i:j]
                    if sub_perm == sub_perm[::-1]:
                        palindromes.add(sub_perm)
    return palindromes