from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    string = s[1:8].lower()
    for p in permutations(string, len(string)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 7:
            result.add(word)
    return result