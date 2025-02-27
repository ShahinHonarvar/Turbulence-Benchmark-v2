def palindromes_of_specific_lengths(text):
    return {word for word in set(text[16:78].lower().split()) if len(word) in range(43, 48) and word == word[::-1] and word.isalpha()}