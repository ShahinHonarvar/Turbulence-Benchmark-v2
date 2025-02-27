from itertools import permutations

def palindromes_between_indices(s):
    substr = s[5:9].lower()
    palindromes = set()
    for i in range(3, len(substr) + 1):
        for perm in permutations(substr, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes