def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[0:8].split()) if len(word) in range(4, 6) and word.lower() == word.lower()[::-1] and word.isalpha()}