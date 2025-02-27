def palindromes_of_specific_lengths(text):
    return {word for word in set(text[17:96].lower()) if word == word[::-1] and 13 <= len(word) <= 49 and word.isalpha()}