import itertools

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[2:10] if c.isalpha())).lower()
    result = set()
    for i in range(6, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                result.add(word)
    return result