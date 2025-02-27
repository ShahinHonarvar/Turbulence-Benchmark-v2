from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    for i in range(3, 7):
        for item in permutations(text[2:7], i):
            word = ''.join(item)
            if word.lower() == word[::-1].lower() and len(word) >= 3:
                result.add(word.lower())
    return result