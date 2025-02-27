def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[10:60].split()) if len(word) in range(18, 37) and word.lower() == word.lower()[::-1] and word.isascii()}