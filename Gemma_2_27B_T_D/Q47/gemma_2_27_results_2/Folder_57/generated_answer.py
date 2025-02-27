def palindromes_of_specific_lengths(text):
    return {word for word in set(text[16:95]) if word.isalpha() and len(word) in range(39, 53) and (word.lower() == word[::-1].lower())}