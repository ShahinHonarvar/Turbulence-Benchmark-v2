def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[13:96].split()) if len(word) in range(57, 61) and word.lower() == word.lower()[::-1] and word.isalpha()}