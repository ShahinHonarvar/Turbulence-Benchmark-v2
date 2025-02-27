def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[10:60].split()) if word.lower() == word.lower()[::-1] and 18 <= len(word) <= 36 and word.isalpha()}