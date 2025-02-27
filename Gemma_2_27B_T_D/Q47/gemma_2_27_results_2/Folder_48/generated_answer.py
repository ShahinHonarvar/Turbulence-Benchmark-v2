def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[155:284].split()) if len(word) in range(104, 121) and word.lower() == word.lower()[::-1] and word.isalpha()}