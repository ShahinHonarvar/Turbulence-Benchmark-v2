import itertools

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[1:7]
    substring_set = set(substring.lower())
    substrings = {''.join(p) for p in itertools.permutations(substring_set) if p[0] in english_letters and all((c in english_letters for c in p))}
    palindromes = {p for p in substrings if p == p[::-1] and len(p) >= 4}
    return palindromes