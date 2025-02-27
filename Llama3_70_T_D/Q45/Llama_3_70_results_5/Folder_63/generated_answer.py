import itertools

def palindromes_between_indices(s):
    s = s[:4].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(3, len(s) + 1):
        for p in itertools.permutations(s, r):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 3:
                palindromes.add(word)
    return palindromes