def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[32:72].split()) if word.lower() == word.lower()[::-1] and 21 <= len(word) <= 32 and word.isalpha()}