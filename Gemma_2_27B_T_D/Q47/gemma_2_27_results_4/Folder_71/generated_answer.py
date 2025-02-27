def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[18:66]) if len(word) in range(23, 37) and word.isalpha() and (word.lower() == word[::-1].lower())}