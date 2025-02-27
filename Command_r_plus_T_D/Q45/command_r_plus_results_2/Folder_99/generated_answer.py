def palindromes_between_indices(s):
    english_letters = ''.join(filter(str.isalpha, s[4:9].lower()))
    return set((word for word in english_letters if english_letters.count(word) >= 2))