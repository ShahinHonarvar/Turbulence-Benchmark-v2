def palindromes_of_specific_lengths(text):
    return {word for word in set(text[33:86].lower().split()) if len(word) in range(26, 32) and word == word[::-1] and word.isalpha()}