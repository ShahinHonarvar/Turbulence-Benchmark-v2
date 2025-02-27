def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[33:86].split()) if len(word) in range(26, 32) and word.lower() == word.lower()[::-1] and word.isalpha()}