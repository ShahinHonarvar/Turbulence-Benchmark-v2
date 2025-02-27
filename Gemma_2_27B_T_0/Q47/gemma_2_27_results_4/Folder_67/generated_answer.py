def palindromes_of_specific_lengths(text):
    return {word for word in set(text[65:100].lower().split()) if len(word) in range(26, 34) and word == word[::-1] and word.isalpha()}