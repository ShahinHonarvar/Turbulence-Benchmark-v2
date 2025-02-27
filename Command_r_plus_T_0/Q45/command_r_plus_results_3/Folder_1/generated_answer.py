import itertools

def palindromes_between_indices(s):
    sub_str = s[4:8].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((char for char in sub_str if char in english_letters))
    arrangements = set((''.join(arr) for arr in itertools.permutations(filtered_sub_str)))
    palindromes = set((arr for arr in arrangements if len(arr) >= 5 and arr == arr[::-1]))
    return palindromes