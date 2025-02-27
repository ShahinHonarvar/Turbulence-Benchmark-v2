def palindromes_of_specific_lengths(text):
    return {word for word in set(text[44:100].lower().split()) if len(word) in range(13, 43) and word == word[::-1] and word.isalpha()}