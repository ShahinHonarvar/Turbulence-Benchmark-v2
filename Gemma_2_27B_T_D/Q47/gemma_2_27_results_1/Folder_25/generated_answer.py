def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[26:85] if len(word) in range(30, 47) and word.lower() == word[::-1] and word.isalpha()}