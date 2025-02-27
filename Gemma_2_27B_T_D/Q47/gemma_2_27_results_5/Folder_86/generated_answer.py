def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[30:96]) if word.lower() == word.lower()[::-1] and 34 <= len(word) <= 55 and word.isalpha()}