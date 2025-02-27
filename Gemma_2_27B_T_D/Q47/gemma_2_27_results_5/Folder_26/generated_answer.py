def palindromes_of_specific_lengths(text):
    return {word for word in [s[24:85] for s in [text]][0].split() if len(word) in range(21, 32) and word.lower()[::-1] == word.lower() and word.isalpha()}