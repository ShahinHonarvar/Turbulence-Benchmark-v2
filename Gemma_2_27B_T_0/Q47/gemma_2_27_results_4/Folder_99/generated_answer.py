def palindromes_of_specific_lengths(text):
    return {word for word in set(text[127:289].lower().split()) if len(word) in range(119, 142) and word == word[::-1] and word.isalpha()}