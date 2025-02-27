def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[11:88]) if len(word) in range(4, 6) and word.lower() == word.lower()[::-1] and word.isalpha()}