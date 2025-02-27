import itertools

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[1:8] if c.isalpha())).lower()
    result = set()
    for i in range(5, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result