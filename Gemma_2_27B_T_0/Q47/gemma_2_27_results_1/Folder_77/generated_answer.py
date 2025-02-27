def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[103:277].split()) if len(word) in range(100, 170) and word.lower() == word.lower()[::-1] and word.isalpha()}