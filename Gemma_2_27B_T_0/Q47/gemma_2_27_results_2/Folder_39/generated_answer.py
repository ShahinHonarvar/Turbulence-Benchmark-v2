def palindromes_of_specific_lengths(text):
    return {word for word in set(text[31:92].lower().split()) if len(word) in range(50, 54) and word == word[::-1] and word.isalpha()}