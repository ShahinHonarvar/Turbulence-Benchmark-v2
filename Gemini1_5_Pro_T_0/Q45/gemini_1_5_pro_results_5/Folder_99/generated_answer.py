from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(3, 6):
        for j in permutations(string[4:9], i):
            word = ''.join(j)
            if word.lower() == word[::-1].lower() and len(word) >= 3:
                result.add(word)
    return result