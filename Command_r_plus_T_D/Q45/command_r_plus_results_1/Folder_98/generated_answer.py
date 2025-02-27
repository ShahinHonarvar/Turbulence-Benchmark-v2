from itertools import permutations

def palindromes_between_indices(s):
    sub = s[3:6]
    english_letters = [char for char in sub if char.isalpha()]
    english_letters = [char.lower() for char in english_letters]
    arrangements = set((''.join(p) for p in permutations(english_letters)))
    palindromes = set((arr for arr in arrangements if arr == arr[::-1] and len(arr) >= 4))
    return palindromes