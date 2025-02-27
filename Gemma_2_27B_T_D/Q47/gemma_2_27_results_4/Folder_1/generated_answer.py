def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[15:90].split()) if len(word) in range(40, 73) and word.lower() == word.lower()[::-1] and word.isalpha()}