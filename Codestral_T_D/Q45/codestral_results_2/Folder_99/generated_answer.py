from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    palindromes = set()
    for r in range(3, len(substring) + 1):
        for perm in permutations(substring, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes