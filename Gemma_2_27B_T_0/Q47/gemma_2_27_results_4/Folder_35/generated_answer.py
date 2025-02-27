def palindromes_of_specific_lengths(text):
    return {word for word in set(text[34:91].lower().split()) if word == word[::-1] and 14 <= len(word) <= 39 and word.isalpha()}