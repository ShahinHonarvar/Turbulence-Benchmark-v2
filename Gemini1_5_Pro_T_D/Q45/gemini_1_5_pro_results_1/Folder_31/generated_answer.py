import itertools

def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = ''.join((c for c in string[1:9] if c.lower() in english_letters)).lower()
    results = set()
    for i in range(6, len(letters) + 1):
        for candidate in itertools.permutations(letters, i):
            word = ''.join(candidate)
            if word == word[::-1]:
                results.add(word)
    return results