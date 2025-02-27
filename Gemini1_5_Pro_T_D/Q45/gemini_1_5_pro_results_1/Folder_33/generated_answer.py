from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(7, 10):
        if string[i].isalpha():
            letters.append(string[i].lower())
    results = set()
    for i in range(4, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and len(word) >= 4:
                results.add(word)
    return results