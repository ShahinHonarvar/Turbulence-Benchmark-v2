def palindromes_of_specific_lengths(text):
    return {word for word in set(text[130:296].lower().split()) if len(word) in range(103, 159) and word == word[::-1] and word.isalpha()}