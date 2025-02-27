def palindromes_of_specific_lengths(text):
    return {word for word in set(text[20:75].lower()) if word == word[::-1] and len(word) in range(36, 43) and word.isalpha()}