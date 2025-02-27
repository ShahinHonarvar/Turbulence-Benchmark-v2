def palindromes_of_specific_lengths(text):
    return {word for word in set(text[23:78].lower().split()) if word == word[::-1] and 13 <= len(word) <= 40 and word.isalpha()}