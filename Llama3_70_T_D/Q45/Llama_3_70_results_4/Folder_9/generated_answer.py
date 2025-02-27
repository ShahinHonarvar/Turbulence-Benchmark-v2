from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 7:
        return set()
    palindromes = set()
    for p in permutations(letters):
        if len(p) >= 7 and p[:len(p) // 2] == p[len(p) // 2 + len(p) % 2:][::-1]:
            palindromes.add(''.join(p))
    return palindromes