def palindromes_of_specific_lengths(text):
    return {word for word in text[2:9].lower().split() if len(word) in (3, 4) and word == word[::-1]}