def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[32:80].split()) if len(word) in range(35, 42) and word.lower() == word.lower()[::-1] and word.isalpha()}