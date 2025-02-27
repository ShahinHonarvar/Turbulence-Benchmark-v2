from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    string = string[1:9]
    for i in range(6, len(string) + 1):
        for item in permutations(string, i):
            word = ''.join(item)
            if word.lower() == word[::-1].lower():
                result.add(word.lower())
    return result