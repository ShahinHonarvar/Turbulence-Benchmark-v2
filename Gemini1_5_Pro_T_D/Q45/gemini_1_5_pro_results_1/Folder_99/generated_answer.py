from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    for item in permutations(text[4:9]):
        word = ''.join(item)
        if len(word) >= 3 and word.lower() == word[::-1].lower():
            result.add(word.lower())
    return result