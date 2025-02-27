def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[22:96].split()) if word.lower() == word.lower()[::-1] and 52 <= len(word) <= 55 and word.isalpha()}