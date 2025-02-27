def palindromes_of_specific_lengths(text):
    return {word for word in set(text[124:284].lower().split()) if len(word) in range(115, 135) and word == word[::-1] and word.isalpha()}