from itertools import permutations

def palindromes_between_indices(string):
    results = set()
    for i in range(4, 7):
        for j in permutations(string[2:9], i):
            word = ''.join(j)
            if word.casefold() == word.casefold()[::-1] and len(word) >= 4:
                results.add(word)
    return results