def palindromes_between_indices(s):
    letters = ''.join(sorted(s[0:4].lower()))
    return set((p for i in range(len(letters)) for j in range(i + 2, len(letters) - 1) for p in [''.join(reversed(letters[i:j + 1])), letters[i:j + 1]]))