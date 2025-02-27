def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[75:96].split()) if len(word) in range(7, 10) and word.lower() == word.lower()[::-1] and word.isalpha()}