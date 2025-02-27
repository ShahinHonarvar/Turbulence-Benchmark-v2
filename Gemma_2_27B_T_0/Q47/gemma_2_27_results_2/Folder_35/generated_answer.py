def palindromes_of_specific_lengths(text):
    return {word for word in set(text[34:91].lower().split()) if len(word) in range(14, 40) and word == word[::-1] and word.isalpha()}