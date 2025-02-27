from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[6:10])).lower()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for p in permutations(letters, length):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes