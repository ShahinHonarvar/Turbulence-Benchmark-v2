def palindromes_of_specific_lengths(text):
    return {word for word in set(text[31:92]) if word.isalpha() and word.lower() == word.lower()[::-1] and (len(word) in range(50, 54))}