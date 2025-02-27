def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[15:87]) if len(word) in range(51, 61) and word.isalpha() and (word.lower() == word.lower()[::-1])}