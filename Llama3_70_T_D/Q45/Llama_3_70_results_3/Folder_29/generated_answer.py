from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(6, len(s) + 1):
        for perm in permutations(s, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes