def palindromes_between_indices(s):
    english_letters = ''.join(filter(str.isalpha, s[6:9].lower()))
    return set((word for word in english_letters if word == word[::-1] and len(word) >= 3))