def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[30:85].split()) if len(word) in range(12, 21) and word.lower() == word.lower()[::-1] and word.isalpha()}