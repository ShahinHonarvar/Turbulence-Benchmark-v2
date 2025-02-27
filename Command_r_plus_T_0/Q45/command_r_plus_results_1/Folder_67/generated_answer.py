def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:7].lower()))
    arrangements = set((letters[i:j] for i in range(len(letters)) for j in range(i + 5, len(letters) + 1)))
    palindromes = set((arr for arr in arrangements if arr == arr[::-1]))
    return palindromes