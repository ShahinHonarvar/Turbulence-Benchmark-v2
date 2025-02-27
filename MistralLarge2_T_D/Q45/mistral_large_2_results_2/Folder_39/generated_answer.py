import itertools

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[2:6])).lower()
    letters = set(substring)
    palindromes = set()
    for r in range(3, len(substring) + 1):
        for p in itertools.permutations(substring, r):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes