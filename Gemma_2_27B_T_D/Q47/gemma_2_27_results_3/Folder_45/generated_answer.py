def palindromes_of_specific_lengths(text):
    return {word for word in set((word.lower() for word in text[70:141].split())) if len(word) in range(3, 61) and word == word[::-1] and word.isalpha()}