def palindromes_of_specific_lengths(text):
    return {word for word in set(text[27:78].lower().split()) if len(word) in range(18, 20) and word == word[::-1] and word.isalpha()}