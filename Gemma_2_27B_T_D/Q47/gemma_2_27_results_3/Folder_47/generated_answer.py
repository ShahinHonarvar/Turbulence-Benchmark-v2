def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[39:95]) if word.isalpha() and len(word) in range(14, 53) and (word.lower() == word.lower()[::-1])}