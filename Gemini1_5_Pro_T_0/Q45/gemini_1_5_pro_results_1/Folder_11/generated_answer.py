from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for item in permutations(string[3:8]):
        word = ''.join(item)
        if len(word) >= 4 and word.lower() == word[::-1].lower():
            result.add(word.lower())
    return result