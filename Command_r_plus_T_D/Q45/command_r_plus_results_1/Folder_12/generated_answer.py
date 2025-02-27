import itertools

def palindromes_between_indices(s):
    sub_str = s[3:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((ch for ch in sub_str if ch in english_letters))
    arrangements = [''.join(p) for p in itertools.permutations(filtered_sub_str)]
    palindromes = set((arr for arr in arrangements if arr == arr[::-1] and len(arr) >= 4))
    return palindromes