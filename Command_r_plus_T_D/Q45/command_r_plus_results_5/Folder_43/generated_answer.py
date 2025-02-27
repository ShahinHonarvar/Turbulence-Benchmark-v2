def palindromes_between_indices(s):
    english_letters = ''.join(filter(str.isalpha, s[2:6].lower()))
    return set((w for w in english_letters if w == w[::-1] and len(w) >= 4))