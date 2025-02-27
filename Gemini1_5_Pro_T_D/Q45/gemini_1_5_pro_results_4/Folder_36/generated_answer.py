from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[5:9] if char.isalpha())).lower()
    results = set()
    for i in range(3, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                results.add(word)
    return results