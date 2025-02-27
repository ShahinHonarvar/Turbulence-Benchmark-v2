def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[15:90]) if len(word) >= 40 and len(word) <= 72 and (word.lower() == word.lower()[::-1]) and word.isalpha()}