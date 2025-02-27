def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[11:88].split() if len(word) in range(4, 6) and word.lower() == word.lower()[::-1] and word.isalpha()}