def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[:8] if len(word) in range(4, 6) and word.lower() == word.lower()[::-1] and word.isalpha()}