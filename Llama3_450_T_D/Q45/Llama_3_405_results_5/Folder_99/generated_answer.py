import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes