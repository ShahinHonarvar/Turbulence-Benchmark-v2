def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[43:96].split()) if word.lower() == word.lower()[::-1] and 18 <= len(word) <= 47 and word.isalpha()}