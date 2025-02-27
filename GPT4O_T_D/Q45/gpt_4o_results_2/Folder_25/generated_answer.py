from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5]
    s = ''.join(filter(str.isalpha, s)).lower()
    results = set()
    if len(s) < 3:
        return results
    for length in range(3, len(s) + 1):
        for combo in permutations(s, length):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                results.add(combo_str)
    return results