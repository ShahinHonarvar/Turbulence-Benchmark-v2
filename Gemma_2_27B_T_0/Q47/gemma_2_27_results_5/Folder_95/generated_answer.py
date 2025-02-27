def palindromes_of_specific_lengths(text):
    return {word for word in set(text[12:57].lower().split()) if len(word) in range(20, 22) and word == word[::-1] and word.isalpha()}