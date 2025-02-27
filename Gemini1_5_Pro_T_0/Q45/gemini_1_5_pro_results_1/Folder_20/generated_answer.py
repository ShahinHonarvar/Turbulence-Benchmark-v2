from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(2, 9):
        for j in permutations(string[2:9], i):
            word = ''.join(j)
            if len(word) >= 4 and word.lower() == word[::-1].lower():
                result.add(word.lower())
    return result