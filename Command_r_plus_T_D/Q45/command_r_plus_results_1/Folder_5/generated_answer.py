def palindromes_between_indices(s):
    s = s[4:9].lower()
    return set((word for word in s if word == word[::-1] and len(word) >= 4))