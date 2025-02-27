def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[29:99].lower().split()) if len(word) in range(6, 10) and word.lower() == word.lower()[::-1] and word.isalpha()}