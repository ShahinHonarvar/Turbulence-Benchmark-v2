def palindromes_of_specific_lengths(text):
    return {word for word in set(text[35:89].lower().split()) if len(word) in range(24, 34) and word == word[::-1] and word.isalpha()}