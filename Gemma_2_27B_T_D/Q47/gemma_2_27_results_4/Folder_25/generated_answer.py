def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[26:85].split()) if len(word) in range(30, 47) and word.lower() == word.lower()[::-1] and word.isalpha()}