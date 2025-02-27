from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for item in permutations(string[1:5]):
        word = ''.join(item)
        if len(word) >= 4 and word.lower() == word[::-1].lower():
            result.add(word.lower())
    return result