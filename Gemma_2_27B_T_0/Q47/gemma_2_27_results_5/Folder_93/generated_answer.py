def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[17:96].split()) if len(word) in range(13, 50) and word.lower() == word.lower()[::-1] and word.isalpha()}