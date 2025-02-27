from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    sub = s[4:8].lower()
    sub_letters = [c for c in sub if c.isalpha()]
    if not sub_letters:
        return set()
    palindromes = set()
    for p in permutations(sub_letters):
        p_str = ''.join(p)
        if p_str == p_str[::-1] and len(p_str) >= 5:
            palindromes.add(p_str)
    return palindromes