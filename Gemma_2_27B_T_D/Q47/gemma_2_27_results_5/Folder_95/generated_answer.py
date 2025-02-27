def palindromes_of_specific_lengths(text):
    return {word for word in set(text[12:57].lower().split()) if word == word[::-1] and 20 <= len(word) <= 21 and word.isalpha()}