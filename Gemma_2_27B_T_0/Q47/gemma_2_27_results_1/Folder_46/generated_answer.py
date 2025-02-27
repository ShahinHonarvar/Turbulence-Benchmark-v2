def palindromes_of_specific_lengths(text):
    return {word for word in set(text[11:98].lower().split()) if len(word) in range(29, 63) and word == word[::-1] and word.isalpha()}