import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:8] if c.isalpha()]
    length = len(letters)
    palindromes = set()
    for l in range(4, length + 1):
        for p in itertools.permutations(letters, l):
            p_str = ''.join(p).lower()
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes