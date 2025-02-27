import itertools

def palindromes_between_indices(s):
    substr = s[2:8]
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for perm in itertools.permutations(substr, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes