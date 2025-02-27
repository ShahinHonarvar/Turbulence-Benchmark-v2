def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[11:84]) if len(word) in range(13, 67) and word.isalpha() and (word.lower() == word.lower()[::-1])}