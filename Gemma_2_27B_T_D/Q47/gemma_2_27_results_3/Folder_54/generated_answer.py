def palindromes_of_specific_lengths(text):
    return {word.lower() for word in text[27:78] if len(word) in range(18, 20) and word.isalpha() and (word.lower() == word[::-1].lower())}