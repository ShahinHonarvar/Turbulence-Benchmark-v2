import itertools

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[2:9] if c.isalpha())).lower()
    result = set()
    for i in range(7, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                result.add(word)
    return result