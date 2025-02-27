import itertools

def palindromes_between_indices(s):
    substring = ''.join([c for c in s[1:6] if c.isalpha()])
    substring = substring.lower()
    pg = itertools.permutations(substring)
    palindromes = set()
    for p in pg:
        word = ''.join(p)
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word)
    return palindromes