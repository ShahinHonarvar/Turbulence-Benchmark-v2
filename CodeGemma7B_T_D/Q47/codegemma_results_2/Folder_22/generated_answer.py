def palindromes_of_specific_lengths(text):
    return {word for word in text.lower()[100:201] if len(word) in range(5, 11) and word == word[::-1]}