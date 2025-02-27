def palindromes_of_specific_lengths(text):
    return {word for word in set(text[11:84].lower().split()) if word == word[::-1] and 13 <= len(word) <= 66 and word.isalpha()}