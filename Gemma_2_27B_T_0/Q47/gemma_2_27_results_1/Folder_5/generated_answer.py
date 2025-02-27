def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[63:71] if word.lower() == word.lower()[::-1] and 4 <= len(word) <= 5 and word.isalpha()}