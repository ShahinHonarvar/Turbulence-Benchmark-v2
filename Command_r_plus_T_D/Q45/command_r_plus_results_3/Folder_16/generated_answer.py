import itertools

def palindromes_between_indices(s):
    sub_str = s[6:10].lower()
    unique_letters = set((ch for ch in sub_str if ch.isalpha()))
    arrangements = set((''.join(arr) for arr in itertools.permutations(unique_letters)))
    palindromes = set((arr for arr in arrangements if len(arr) >= 5 and arr == arr[::-1]))
    return palindromes