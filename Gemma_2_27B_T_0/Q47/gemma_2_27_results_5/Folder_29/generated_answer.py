def palindromes_of_specific_lengths(text):
    return {word for word in set(text[15:95].lower().split()) if word == word[::-1] and 18 <= len(word) <= 73 and word.isalpha()}