from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(3, 8):
        for j in permutations(string[3:8], i):
            word = ''.join(j)
            if len(word) >= 4 and word.lower() == word[::-1].lower():
                result.add(word.lower())
    return result