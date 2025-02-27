from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    letters = [ch for ch in s if ch.isalpha()]
    permutations_set = set(permutations(letters))
    palindromes_set = set()
    for perm in permutations_set:
        if len(perm) < 4:
            continue
        for i in range(4, len(perm) + 1):
            for sub_perm in permutations(perm, i):
                sub_perm_str = ''.join(sub_perm)
                if sub_perm_str == sub_perm_str[::-1]:
                    palindromes_set.add(sub_perm_str)
    return {p for p in palindromes_set if len(p) >= 4}