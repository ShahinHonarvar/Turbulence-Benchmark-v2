def palindromes_of_specific_lengths(text):
    return {word for word in set(text[26:88].lower().split()) if len(word) in range(52, 57) and word == word[::-1] and word.isalpha()}