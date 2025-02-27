from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    for l in range(5, len(s) + 1):
        for perm in permutations(s, l):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes