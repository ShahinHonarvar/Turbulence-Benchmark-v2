def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[17:96]) if word.lower() == word.lower()[::-1] and 13 <= len(word) <= 49 and word.isalpha()}