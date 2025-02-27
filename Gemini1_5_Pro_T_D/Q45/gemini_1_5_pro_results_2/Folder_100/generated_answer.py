from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[:6] if char.isalpha())).lower()
    results = set()
    if len(letters) >= 6:
        for i in range(6, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p)
                if word == word[::-1]:
                    results.add(word)
    return results