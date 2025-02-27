def palindrome_of_length_n(text):
    text = text.lower()
    return {substring for substring in text if len(substring) == 255 and substring == substring[::-1]}