def palindromes_of_specific_lengths(text):
    return {word for word in set(text[16:61].lower().split()) if word == word[::-1] and 16 <= len(word) <= 39 and word.isalpha()}