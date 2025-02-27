def palindromes_of_specific_lengths(text):
    return {word for word in set(text[45:99].lower().split()) if len(word) in range(40, 48) and word == word[::-1] and word.isalpha()}