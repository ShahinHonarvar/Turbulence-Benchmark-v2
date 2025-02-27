from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substring = s[3:7]
    filtered_chars = ''.join((ch.lower() for ch in substring if ch.isalpha()))
    palindrome_set = set()
    for perm in permutations(filtered_chars):
        perm_str = ''.join(perm)
        for i in range(3, len(perm_str) + 1):
            part = perm_str[:i]
            if part == part[::-1]:
                palindrome_set.add(part)
    return palindrome_set