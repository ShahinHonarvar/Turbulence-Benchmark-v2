def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[1:9] if len(word) in (3, 4) and word.lower() == word.lower()[::-1] and word.isalpha()}