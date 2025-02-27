def palindromes_of_specific_lengths(text):
    return {word for word in set(text[36:93].lower()) if word == word[::-1] and 10 <= len(word) <= 35 and word.isalpha()}