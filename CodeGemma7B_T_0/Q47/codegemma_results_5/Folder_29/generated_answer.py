def palindromes_of_specific_lengths(text):
    return {word for word in text.lower().split() if 15 <= text.index(word) <= 94 and 18 <= len(word) <= 73 and (word == word[::-1])}