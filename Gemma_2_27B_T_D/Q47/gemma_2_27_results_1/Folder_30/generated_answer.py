def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[14:91]) if word.lower() == word.lower()[::-1] and 55 <= len(word) <= 71 and word.isalpha()}