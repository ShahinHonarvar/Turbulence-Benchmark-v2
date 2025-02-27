def palindromes_of_specific_lengths(text):
    return {word for word in set(text[18:89].lower().split()) if len(word) in range(12, 15) and word == word[::-1] and word.isalpha()}