def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[18:89]) if len(word) in range(12, 15) and word.lower() == word.lower()[::-1] and word.isalpha()}