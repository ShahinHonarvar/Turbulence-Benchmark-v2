def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[31:92]) if len(word) in range(50, 54) and word.lower() == word[::-1].lower() and word.isalpha()}