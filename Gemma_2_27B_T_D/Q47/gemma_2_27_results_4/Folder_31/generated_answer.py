def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[11:84]) if len(word) in range(37, 61) and word.isalpha() and (word.lower() == word[::-1].lower())}