from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    if len(letters) < 6:
        return set()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for p in permutations(letters, length):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes