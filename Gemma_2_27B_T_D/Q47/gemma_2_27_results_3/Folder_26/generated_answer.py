def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[24:85].split()) if len(word) in range(21, 32) and word.lower() == word.lower()[::-1] and word.isalpha()}