import itertools

def palindromes_between_indices(s):
    s = s[0:8].lower()
    palindromes = set()
    for i in range(7, len(s) + 1):
        for p in itertools.permutations(s, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes