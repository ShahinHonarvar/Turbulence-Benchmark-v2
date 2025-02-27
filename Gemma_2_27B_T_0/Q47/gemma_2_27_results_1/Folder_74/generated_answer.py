def palindromes_of_specific_lengths(text):
    return {word for word in set(text[30:85].lower().split()) if len(word) in range(12, 21) and word == word[::-1] and word.isalpha()}