def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[70:141].split()) if word.lower() == word.lower()[::-1] and 3 <= len(word) <= 60 and word.isalpha()}