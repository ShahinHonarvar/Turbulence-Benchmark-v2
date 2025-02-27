from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for item in permutations(string[3:7], 4):
        word = ''.join(item)
        if word.lower() == word[::-1].lower() and len(word) >= 4:
            result.add(word.lower())
    return result