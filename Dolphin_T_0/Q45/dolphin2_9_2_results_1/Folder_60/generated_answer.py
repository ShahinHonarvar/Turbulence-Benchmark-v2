from itertools import product, permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:7]]
    palindromes = set()
    for p in product(letters, repeat=len(letters)):
        for pals in permutations(p):
            word = ''.join(pals)
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes