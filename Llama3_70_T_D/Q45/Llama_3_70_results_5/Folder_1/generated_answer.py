from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[4:8].lower()
    palindromes = set()
    for r in range(5, len(s) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1] and set(word).issubset(set(s)):
                palindromes.add(word)
    return palindromes