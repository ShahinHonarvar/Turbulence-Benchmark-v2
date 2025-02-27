def palindromes_of_specific_lengths(text):
    return {word for word in set((word.lower() for word in text[13:96].split() if len(word) in range(57, 61) and word.isalnum() and (word == word[::-1])))}