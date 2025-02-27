def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[10:101].split() if len(word) in range(10, 51) and word.lower() == word.lower()[::-1] and word.isalpha()}