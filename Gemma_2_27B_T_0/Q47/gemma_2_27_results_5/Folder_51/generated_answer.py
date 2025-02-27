def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[2:9] if word.lower() == word.lower()[::-1] and 3 <= len(word) <= 4 and word.isalpha()}