def palindromes_of_specific_lengths(text):
    return {word for word in set(text[16:95].lower().split()) if len(word) in range(39, 53) and word == word[::-1] and word.isalpha()}