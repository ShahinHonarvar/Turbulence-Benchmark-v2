def palindromes_of_specific_lengths(text):
    return {word for word in set(text[155:284].lower().split()) if len(word) in range(104, 121) and word == word[::-1] and word.isalpha()}