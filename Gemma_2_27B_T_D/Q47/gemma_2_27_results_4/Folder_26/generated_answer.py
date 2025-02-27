def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[24:85].split()) if word.lower() == word.lower()[::-1] and 21 <= len(word) <= 31 and word.isalpha()}