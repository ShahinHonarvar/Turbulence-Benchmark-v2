def palindromes_of_specific_lengths(text):
    return {word for word in set(text[32:80].lower().split()) if len(word) in range(35, 42) and word == word[::-1] and word.isalpha()}