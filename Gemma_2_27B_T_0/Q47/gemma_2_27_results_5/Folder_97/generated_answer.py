def palindromes_of_specific_lengths(text):
    return {word for word in set(text[28:95].lower().split()) if len(word) in range(38, 50) and word == word[::-1] and word.isalpha()}