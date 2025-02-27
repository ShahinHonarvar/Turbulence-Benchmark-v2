def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[28:95].split()) if len(word) in range(38, 50) and word.lower() == word.lower()[::-1] and word.isalpha()}