import re
    from collections import defaultdict

def palindromes_between_indices(s):
    english_indices = set(range(ord('a'), ord('z') + 1))
    letters = set((ord(c) for c in s[0:6] if ord('a') <= ord(c) <= ord('z')))
    if not letters:
        return set()
    perms = set()
    for l in letters:
        perms.add(''.join(sorted(s[0:6], key=lambda c: l if c == chr(l) else 1)))
    palindromes = set()
    for perm in perms:
        for i in range(6, len(perm) + 1):
            if perm[:i] == perm[i - 1::-1] and len(perm[:i]) >= 6:
                palindromes.add(perm[:i])
    palindromes = {''.join((c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(palindrome))) for palindrome in palindromes}
    return palindromes