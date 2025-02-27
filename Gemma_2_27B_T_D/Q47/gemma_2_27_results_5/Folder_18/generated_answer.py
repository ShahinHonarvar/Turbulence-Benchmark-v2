def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[11:84].split()) if word.lower() == word.lower()[::-1] and 13 <= len(word) <= 66 and word.isalpha()}