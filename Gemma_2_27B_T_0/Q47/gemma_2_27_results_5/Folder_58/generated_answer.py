def palindromes_of_specific_lengths(text):
    return {word for word in set(text[125:284].lower().split()) if len(word) in range(109, 127) and word == word[::-1] and word.isalpha()}