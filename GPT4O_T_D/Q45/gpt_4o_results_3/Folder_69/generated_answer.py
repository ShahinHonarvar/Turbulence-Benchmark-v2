from itertools import permutations

def palindromes_between_indices(s):
    s_sub = s[:4].lower()
    letters = [c for c in s_sub if c.isalpha()]
    results = set()
    for length in range(4, len(letters) + 1):
        for p in permutations(letters, length):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                results.add(p_str)
    return results