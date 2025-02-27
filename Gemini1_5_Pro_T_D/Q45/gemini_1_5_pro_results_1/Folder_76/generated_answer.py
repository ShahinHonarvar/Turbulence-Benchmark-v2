from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(4, len(string) + 1):
        for s in permutations(string[1:5], i):
            word = ''.join(s)
            if word.lower() == word[::-1].lower() and len(word) >= 4:
                result.add(word.lower())
    return result