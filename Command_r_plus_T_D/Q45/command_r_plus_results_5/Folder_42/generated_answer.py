def palindromes_between_indices(s):
    s = s[6:10].lower()
    return set((word for word in s if word == word[::-1] and len(word) >= 3))