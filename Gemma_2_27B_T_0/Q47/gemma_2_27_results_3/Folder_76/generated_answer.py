def palindromes_of_specific_lengths(text):
    return {word for word in set(text[101:293].lower().split()) if len(word) in range(154, 183) and word == word[::-1] and word.isalpha()}