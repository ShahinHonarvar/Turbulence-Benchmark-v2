from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10]
    palindromes = set()
    for p in range(5, len(substring) + 1):
        for perm in permutations(substring.lower(), p):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes