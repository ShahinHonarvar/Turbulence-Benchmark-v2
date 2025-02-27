from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:8]
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes