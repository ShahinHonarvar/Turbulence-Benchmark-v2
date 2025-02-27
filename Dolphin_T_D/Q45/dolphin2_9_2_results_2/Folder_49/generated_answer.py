import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:8]))
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters, i):
            word = ''.join(perm).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes