def palindromes_of_specific_lengths(text):
    return {word for word in set(text[14:91].lower().split()) if len(word) in range(55, 72) and word == word[::-1] and word.isalpha()}