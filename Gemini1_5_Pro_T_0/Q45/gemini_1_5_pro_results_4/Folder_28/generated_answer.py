from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(1, 6):
        for j in permutations(string[1:6], i):
            word = ''.join(j)
            if len(word) >= 4 and word.lower() == word[::-1].lower():
                result.add(word.lower())
    return result