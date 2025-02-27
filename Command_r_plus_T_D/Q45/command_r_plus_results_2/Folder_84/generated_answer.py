from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[4:10].lower()
    letters = [char for char in sub_str if char.isalpha()]
    all_arrangements = set((''.join(p) for p in permutations(letters)))
    palindromes = set((arr for arr in all_arrangements if arr == arr[::-1] and len(arr) >= 3))
    return palindromes