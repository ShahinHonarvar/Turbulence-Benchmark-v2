from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(set(s[5:10])))
    palindromes = set()
    for L in range(6, len(letters) + 1):
        for perm in permutations(letters, L):
            word = ''.join(perm)
            if word == word.lower() and word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes