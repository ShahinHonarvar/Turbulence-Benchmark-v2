def palindromes_of_specific_lengths(text):
    return {word for word in set(text[119:257]) if word.isalpha() and word.lower() == word[::-1].lower() and (104 <= len(word) <= 123)}