def palindromes_of_specific_lengths(text):
    return {word for word in set(text[39:95].lower().split()) if word == word[::-1] and len(word) in range(14, 53) and word.isalpha()}