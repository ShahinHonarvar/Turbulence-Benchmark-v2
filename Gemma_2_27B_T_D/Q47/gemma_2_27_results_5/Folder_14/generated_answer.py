def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[10:75]) if word.lower() == word.lower()[::-1] and 6 <= len(word) <= 8 and word.isalpha()}