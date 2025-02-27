def palindromes_of_specific_lengths(text):
    return {word for word in set(text[43:96].lower().split()) if word == word[::-1] and 18 <= len(word) <= 47 and word.isalpha()}