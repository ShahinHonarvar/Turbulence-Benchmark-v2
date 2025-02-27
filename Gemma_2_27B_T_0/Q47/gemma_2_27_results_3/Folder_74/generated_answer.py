def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[30:85]) if word.lower() == word.lower()[::-1] and 12 <= len(word) <= 20 and word.isalpha()}