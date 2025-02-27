def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[21:63].lower().split()) if word.lower() == word.lower()[::-1] and 22 <= len(word) <= 33 and word.isalpha()}