def palindromes_of_specific_lengths(text):
    return {word for word in set(text[40:95].lower().split()) if len(word) in range(45, 52) and word == word[::-1] and word.isalpha()}