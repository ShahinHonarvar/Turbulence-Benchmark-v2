from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    s_sub = ''.join([c.lower() for c in s[4:10] if c.isalpha()])
    palindromes = set()
    for p in permutations(s_sub):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes