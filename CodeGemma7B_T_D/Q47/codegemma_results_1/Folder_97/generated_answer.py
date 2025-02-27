def palindromes_of_specific_lengths(text):
    text = text.lower()
    return {word for word in text[28:95] if word == word[::-1] and 38 <= len(word) <= 49}