import string
    from itertools import permutations

def palindromes_between_indices(s):
    letters = string.ascii_lowercase
    sub_str = s[2:9]
    palindromes = set()
    for p in range(5, len(sub_str) + 1):
        for perm in permutations(sub_str, p):
            pal_str = ''.join(perm)
            pal_str_lower = pal_str.lower()
            if pal_str_lower in palindromes or pal_str_lower[::-1] in palindromes:
                continue
            is_pal = all((pal_str_lower[i] in letters and pal_str_lower[i] == pal_str_lower[~i] for i in range(p // 2)))
            if is_pal:
                palindromes.add(pal_str_lower)
    return palindromes