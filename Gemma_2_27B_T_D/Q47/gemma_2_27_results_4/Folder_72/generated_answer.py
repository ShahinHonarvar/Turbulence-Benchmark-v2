def palindromes_of_specific_lengths(text):
    return {word for word in set(text[26:91].lower().split()) if word == word[::-1] and 27 <= len(word) <= 58 and word.isalpha()}