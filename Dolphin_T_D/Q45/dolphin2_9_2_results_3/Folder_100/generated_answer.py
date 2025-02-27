from itertools import permutations

def palindromes_between_indices(s):
    if not all((c.isalpha() or c.isdigit() for c in s)):
        return set()
    s = ''.join((c for c in s if c.isalpha()))
    n = len(s)
    palindromes = set()
    for p in permutations(s, n):
        if len(set(p)) != n or len(p) < 6:
            continue
        for i in range(n - 5):
            text = ''.join(p[i:i + n])
            if text == text[::-1]:
                palindromes.add(text)
    return palindromes