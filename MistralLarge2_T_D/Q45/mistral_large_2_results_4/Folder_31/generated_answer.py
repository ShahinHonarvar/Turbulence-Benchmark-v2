from itertools import permutations

def palindromes_between_indices(s):
    letters = [ch for ch in s[1:9] if ch.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for p in permutations(letters, length):
            p_str = ''.join(p).lower()
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes