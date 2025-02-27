import itertools

def palindromes_between_indices(s):
    s = s[5:10].lower()
    palindromes = set()
    for r in range(5, len(s) + 1):
        for combination in itertools.permutations(s, r):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes