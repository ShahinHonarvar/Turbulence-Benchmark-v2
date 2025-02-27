def palindromes_of_specific_lengths(text):
    return {word for word in text[62:89].lower() if word == word[::-1] and len(word) in range(18, 22) and word.isalpha()}