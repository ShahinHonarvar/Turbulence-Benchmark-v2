def palindromes_of_specific_lengths(text):
    return {word for word in [text[i:i + l] for i in range(10, 56) for l in range(3, 8)] if word.isalpha() and word == word[::-1]}