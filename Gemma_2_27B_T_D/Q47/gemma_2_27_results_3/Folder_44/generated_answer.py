def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[18:99]) if word.lower() == word.lower()[::-1] and len(word) in range(31, 52)}