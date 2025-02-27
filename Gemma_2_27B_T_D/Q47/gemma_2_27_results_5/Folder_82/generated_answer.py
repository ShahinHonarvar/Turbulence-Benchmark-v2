def palindromes_of_specific_lengths(text):
    return {word for word in set(text[3:301].lower().split()) if word == word[::-1] and 30 <= len(word) <= 300 and word.isalpha()}