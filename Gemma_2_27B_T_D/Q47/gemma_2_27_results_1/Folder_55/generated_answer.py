def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[10:76].split()) if len(word) in range(10, 21) and word.lower() == word.lower()[::-1] and word.isalpha()}