from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([c for c in text[2:5] if c.isalpha()]).lower()
    results = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                results.add(word)
    return results