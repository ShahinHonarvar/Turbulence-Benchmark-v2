def palindromes_of_specific_lengths(text):
    return {word for word in set(text[11:94].lower().split()) if len(word) in range(34, 55) and word == word[::-1] and word.isalpha()}