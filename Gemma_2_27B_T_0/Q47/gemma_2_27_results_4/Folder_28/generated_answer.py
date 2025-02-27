def palindromes_of_specific_lengths(text):
    return {word for word in set(text[32:72].lower().split()) if len(word) in range(21, 33) and word == word[::-1] and word.isalpha()}