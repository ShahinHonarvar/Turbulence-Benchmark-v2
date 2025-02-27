from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:9].lower()
    palindromes = set()
    for i in range(6, len(substr) + 1):
        for p in permutations(substr, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes