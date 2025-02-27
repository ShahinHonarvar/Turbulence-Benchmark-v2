def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[65:100].split() if len(word) in range(26, 34) and word.lower() == word.lower()[::-1] and word.isalpha()}