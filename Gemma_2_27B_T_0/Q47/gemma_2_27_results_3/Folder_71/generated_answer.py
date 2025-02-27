def palindromes_of_specific_lengths(text):
    return {word for word in set(text[18:66].lower().split()) if len(word) in range(23, 37) and word == word[::-1] and word.isalpha()}