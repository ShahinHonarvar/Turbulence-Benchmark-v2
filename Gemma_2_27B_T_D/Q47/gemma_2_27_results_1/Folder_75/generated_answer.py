def palindromes_of_specific_lengths(text):
    return {word for word in set(text[31:75]) if word.isalpha() and word.lower() == word.lower()[::-1] and (23 <= len(word) <= 39)}