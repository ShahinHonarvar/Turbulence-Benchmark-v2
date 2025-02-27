def palindromes_of_specific_lengths(text):
    return {word for word in set(text[12:93].lower().split()) if word == word[::-1] and 42 <= len(word) <= 77 and word.isalpha()}