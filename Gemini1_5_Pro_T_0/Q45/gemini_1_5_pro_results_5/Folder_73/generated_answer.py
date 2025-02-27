from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for item in permutations(string[3:7], r=None):
        word = ''.join(item)
        if len(word) >= 3 and word.casefold() == ''.join(reversed(word)).casefold():
            result.add(word.casefold())
    return result