def palindromes_of_specific_lengths(text):
    return {word for word in text.lower()[16:95].split() if len(word) in range(39, 53) and word == word[::-1]}