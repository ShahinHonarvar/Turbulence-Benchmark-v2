def palindromes_of_specific_lengths(text):
    return {word for word in set(text[23:83].lower().split()) if len(word) in range(32, 35) and word == word[::-1] and word.isalpha()}