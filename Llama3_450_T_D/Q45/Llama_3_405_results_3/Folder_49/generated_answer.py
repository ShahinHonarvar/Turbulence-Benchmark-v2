import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[5:8] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            ss = ''.join(combo)
            if ss == ss[::-1]:
                palindromes.add(ss)
    return palindromes