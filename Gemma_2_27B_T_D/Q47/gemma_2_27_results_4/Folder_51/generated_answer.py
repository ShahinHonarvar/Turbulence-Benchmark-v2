def palindromes_of_specific_lengths(text):
    return {word for word in set(text[2:9].lower().split()) if len(word) in range(3, 5) and word == word[::-1]}