from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    result = set()
    for p in permutations(s):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            result.add(word)
    return result