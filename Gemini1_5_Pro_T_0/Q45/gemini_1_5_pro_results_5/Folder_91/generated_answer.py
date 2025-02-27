from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(3, 7):
        for j in permutations(string[2:7], i):
            word = ''.join(j)
            if word.lower() == word[::-1].lower():
                result.add(word)
    return result