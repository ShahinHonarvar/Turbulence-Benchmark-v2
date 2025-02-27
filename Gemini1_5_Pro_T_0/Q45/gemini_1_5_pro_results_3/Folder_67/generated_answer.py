from itertools import permutations

def palindromes_between_indices(string):
    s = set()
    for i in permutations(string[2:7]):
        word = ''.join(i)
        if len(word) >= 5 and word.lower() == word[::-1].lower():
            s.add(word.lower())
    return s