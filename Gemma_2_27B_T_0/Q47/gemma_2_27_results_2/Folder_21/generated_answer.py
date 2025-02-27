def palindromes_of_specific_lengths(text):
    return {word for word in set(text[100:296].lower().split()) if len(word) in range(136, 161) and word == word[::-1] and word.isalpha()}