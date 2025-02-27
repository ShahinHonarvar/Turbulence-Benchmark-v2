def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[65:100].lower().split()) if word.lower()[::-1] == word.lower() and 26 <= len(word) <= 33 and word.isalpha()}