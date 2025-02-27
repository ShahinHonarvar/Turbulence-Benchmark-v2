def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[26:91].split()) if len(word) in range(27, 59) and word.lower() == word[::-1].lower() and word.isalpha()}