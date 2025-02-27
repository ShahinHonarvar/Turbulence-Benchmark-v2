def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[11:97] if word.lower() == word.lower()[::-1] and 45 <= len(word) <= 52 and word.isalpha()}