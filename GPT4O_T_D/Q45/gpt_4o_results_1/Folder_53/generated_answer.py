from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9]
    filtered_chars = [c.lower() for c in substring if c.isalpha()]
    perm_set = set()
    length = len(filtered_chars)
    if length < 6:
        return set()
    for chars in permutations(filtered_chars):
        if length == 6 and chars == chars[::-1]:
            perm_set.add(''.join(chars))
        if length > 6:
            for i in range(6, length + 1):
                candidate = chars[:i]
                if candidate == candidate[::-1]:
                    perm_set.add(''.join(candidate))
    return perm_set