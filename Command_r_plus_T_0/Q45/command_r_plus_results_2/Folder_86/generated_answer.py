def palindromes_between_indices(s):
    sub_str = s[6:10].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_str = ''.join(filter(lambda x: x in english_letters, sub_str))
    arrangements = set()
    for p in range(len(sub_str) + 1):
        arrangements.update([''.join(arr) for arr in permutations(sub_str, p)])
    palindromes = set((arr for arr in arrangements if arr == arr[::-1] and len(arr) >= 4))
    return palindromes