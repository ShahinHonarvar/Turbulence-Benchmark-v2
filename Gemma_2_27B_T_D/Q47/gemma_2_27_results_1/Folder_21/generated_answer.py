def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[100:296]) if len(word) in range(136, 161) and word.lower() == word.lower()[::-1] and word.isalpha()}