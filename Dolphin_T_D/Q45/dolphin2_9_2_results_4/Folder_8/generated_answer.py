from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:6] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 5):
        for i in range(2 ** 5):
            w = ''.join((c for c, b in zip(p, bin(i)[2:].zfill(5)) if b == '1'))
            if len(w) >= 5 and w.lower() == w.lower()[::-1]:
                palindromes.add(w.lower())
    return palindromes