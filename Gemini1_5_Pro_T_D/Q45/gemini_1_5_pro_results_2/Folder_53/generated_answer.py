from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(6, len(string[4:9]) + 1):
        for item in permutations(string[4:9], i):
            word = ''.join(item)
            if word.lower() == word[::-1].lower():
                result.add(word.lower())
    return result