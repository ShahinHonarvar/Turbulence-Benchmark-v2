def palindromes_of_specific_lengths(text):
    return {word for word in set(text[75:96].lower().split()) if len(word) in range(7, 10) and word == word[::-1] and word.isalpha()}