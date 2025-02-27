from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    s = ''.join((c for c in text[4:10] if c.isalpha())).lower()
    for i in range(5, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result