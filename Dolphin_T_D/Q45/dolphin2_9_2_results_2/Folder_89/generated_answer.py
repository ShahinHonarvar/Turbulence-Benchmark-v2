import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    if len(set(letters)) < 3:
        return set()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for letters_r in itertools.permutations(letters, r):
            for p in itertools.product(*[letters_r[i:] for i in range(len(letters_r))]):
                if p == p[::-1] and all((c in letters for c in ''.join(p))):
                    palindromes.add(''.join(p))
    return palindromes