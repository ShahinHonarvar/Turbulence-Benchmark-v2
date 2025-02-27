from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    s = text[2:9].lower()
    for i in range(4, len(s) + 1):
        for x in permutations(s):
            word = ''.join(x)[:i]
            if word == word[::-1] and len(word) >= 4:
                result.add(word)
    return result