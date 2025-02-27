import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:8] if c.isalpha()]
    letters = [l.lower() for l in letters]
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for p in itertools.permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes