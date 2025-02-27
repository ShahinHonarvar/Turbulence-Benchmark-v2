def palindromes_of_specific_lengths(text):
    return {word for word in set(text[200:301].lower().split()) if word == word[::-1] and len(word) in range(10, 51) and word.isalpha()}