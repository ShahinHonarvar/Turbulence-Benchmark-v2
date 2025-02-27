def palindromes_of_specific_lengths(text):
    return {word for word in set(text[15:87].lower().split()) if len(word) in range(51, 61) and word == word[::-1] and word.isalpha()}