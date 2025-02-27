from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    s = text[4:8]
    s = ''.join((ch for ch in s if ch.isalnum()))
    for i in range(5, len(s) + 1):
        for p in permutations(s.lower(), i):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 5:
                result.add(word)
    return result