def palindromes_of_specific_lengths(text):
    return {word for word in set(text[26:85].lower().split()) if len(word) in range(30, 47) and word == word[::-1] and word.isalpha()}