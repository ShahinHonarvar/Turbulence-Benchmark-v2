from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for item in permutations(string[2:6]):
        word = ''.join(item)
        if len(word) >= 3 and word.lower() == word[::-1].lower():
            result.add(word.lower())
    return result