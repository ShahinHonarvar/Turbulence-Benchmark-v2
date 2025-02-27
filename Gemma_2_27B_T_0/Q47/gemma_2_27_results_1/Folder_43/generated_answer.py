def palindromes_of_specific_lengths(text):
    return {word for word in set(text[41:90].lower().split()) if len(word) in range(23, 39) and word == word[::-1] and word.isalpha()}