def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[26:88]) if word.lower() == word.lower()[::-1] and 52 <= len(word) <= 56 and word.isalpha()}