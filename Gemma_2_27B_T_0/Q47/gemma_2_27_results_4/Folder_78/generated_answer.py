def palindromes_of_specific_lengths(text):
    return {word for word in set(text[15:73].lower().split()) if len(word) in range(19, 56) and word == word[::-1] and word.isalpha()}