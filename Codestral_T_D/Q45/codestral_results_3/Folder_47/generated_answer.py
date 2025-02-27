from itertools import permutations

def palindromes_between_indices(string):
    substring = string[3:8].lower()
    arrangements = set(permutations(substring, r=None))
    palindromes = {arr for arr in arrangements if arr == arr[::-1] and len(arr) >= 5}
    return palindromes