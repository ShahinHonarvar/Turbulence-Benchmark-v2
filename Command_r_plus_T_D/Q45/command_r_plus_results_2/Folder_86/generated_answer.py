import itertools

def palindromes_between_indices(s):
    sub_str = s[6:10].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((c for c in sub_str if c in english_letters))
    arrangements = [''.join(p) for p in itertools.permutations(filtered_sub_str)]
    palindromes = set((arr for arr in arrangements if len(arr) >= 4 and arr == arr[::-1]))
    return palindromes