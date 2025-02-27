from itertools import combinations_with_replacement

def palindromes_between_indices(s):
    s = s[1:7].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for combo in combinations_with_replacement(s, 4):
        for p in [''.join(combo), ''.join(combo[:-1] + combo[:-2:-1])]:
            if p == p[::-1]:
                palindromes.add(p)
    for combo in combinations_with_replacement(s, 5):
        for p in [''.join(combo), ''.join(combo[:-1] + combo[:-3:-1])]:
            if p == p[::-1]:
                palindromes.add(p)
    for combo in combinations_with_replacement(s, 6):
        for p in [''.join(combo), ''.join(combo[:-1] + combo[:-4:-1])]:
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes