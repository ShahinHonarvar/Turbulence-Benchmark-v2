def palindromes_of_specific_lengths(text):
    palindromes = {word.upper() for word in text.upper().split() if len(word) in range(50, 61) and text.upper().index(word) in range(0, 301)}
    return palindromes