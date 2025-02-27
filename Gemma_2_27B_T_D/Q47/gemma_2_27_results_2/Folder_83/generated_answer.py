def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[75:96]) if word.lower() == word.lower()[::-1] and 7 <= len(word) <= 9 and word.isalpha()}