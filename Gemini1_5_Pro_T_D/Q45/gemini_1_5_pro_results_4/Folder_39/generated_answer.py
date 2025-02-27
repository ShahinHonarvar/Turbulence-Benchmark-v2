from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    for i in range(3, len(text[2:6]) + 1):
        for item in permutations(text[2:6], i):
            word = ''.join(item)
            if word.casefold() == word[::-1].casefold():
                result.add(word)
    return result