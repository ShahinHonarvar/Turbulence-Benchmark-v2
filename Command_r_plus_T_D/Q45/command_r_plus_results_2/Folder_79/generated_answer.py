def palindromes_between_indices(s):
    letters = [c for c in s[1:8] if c.isalpha()]
    arrangements = []
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            arrangements.append(''.join(letters[i:j]))
    palindromes = set((arr for arr in arrangements if arr == arr[::-1] and len(arr) >= 3))
    return palindromes