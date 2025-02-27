from itertools import permutations

def palindromes_between_indices(string):
    s = set()
    for item in permutations(string[0:5], 4):
        word = ''.join(item)
        if word.lower() == word[::-1].lower():
            s.add(word.lower())
    for item in permutations(string[0:5], 5):
        word = ''.join(item)
        if word.lower() == word[::-1].lower():
            s.add(word.lower())
    return s