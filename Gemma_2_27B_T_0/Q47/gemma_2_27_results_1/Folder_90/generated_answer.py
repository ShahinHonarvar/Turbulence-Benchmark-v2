def palindromes_of_specific_lengths(text):
    return {word for word in set(text[106:281].lower().split()) if len(word) in range(136, 152) and word == word[::-1] and word.isalpha()}