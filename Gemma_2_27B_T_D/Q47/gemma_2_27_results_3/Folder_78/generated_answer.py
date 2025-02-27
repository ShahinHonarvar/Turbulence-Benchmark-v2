def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[15:73]) if word.lower() == word.lower()[::-1] and len(word) in range(19, 56) and word.isalpha()}