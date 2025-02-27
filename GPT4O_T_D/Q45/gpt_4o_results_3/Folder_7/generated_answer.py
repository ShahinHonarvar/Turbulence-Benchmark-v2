from itertools import permutations

def palindromes_between_indices(s):
    extracted = ''.join((c.lower() for c in s[1:10] if c.isalpha()))
    palindrome_set = set()
    if len(extracted) < 7:
        return palindrome_set
    for perm in permutations(extracted, len(extracted)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 7:
            palindrome_set.add(perm_str)
    return palindrome_set