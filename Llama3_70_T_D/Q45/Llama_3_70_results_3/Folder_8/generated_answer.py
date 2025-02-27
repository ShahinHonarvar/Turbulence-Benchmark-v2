def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[1:6])).lower()
    return set((''.join(p) for p in __import__('itertools').permutations(s) if len(set(p)) > 1 and len(p) >= 5 and (''.join(p) == ''.join(p)[::-1])))