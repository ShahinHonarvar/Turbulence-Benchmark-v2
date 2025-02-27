def palindromes_of_specific_lengths(text):
    return {word for word in set(text[119:257].lower().split()) if len(word) in range(104, 124) and word == word[::-1] and word.isalpha()}