def palindromes_of_specific_lengths(text):
    return {word for word in set(text[13:100].lower().split()) if len(word) in range(26, 30) and word == word[::-1]}