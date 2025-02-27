def palindromes_between_indices(s):
    letters = set(filter(str.isalpha, s[2:4].lower()))
    arrangements = set((''.join(arr) for arr in set(itertools.permutations(letters))))
    palindromes = set((arr for arr in arrangements if arr == arr[::-1] and len(arr) >= 3))
    return palindromes