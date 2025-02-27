def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[27:78].split()) if len(word) in range(18, 20) and word.lower() == word.lower()[::-1] and word.isalpha()}