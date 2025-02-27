def palindromes_of_specific_lengths(text):
    return {word for word in set(text[12:93].lower().split()) if len(word) in range(17, 67) and word == word[::-1] and word.isalpha()}