from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:7] if char.isalpha())).lower()
    pals = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                pals.add(candidate)
    return pals