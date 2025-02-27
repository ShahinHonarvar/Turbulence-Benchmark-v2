from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10]
    substring = ''.join([char.lower() for char in substring])
    palindromes = set()
    for p in range(5, len(substring) + 1):
        for perm in permutations(substring, p):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes if palindromes else '{}'