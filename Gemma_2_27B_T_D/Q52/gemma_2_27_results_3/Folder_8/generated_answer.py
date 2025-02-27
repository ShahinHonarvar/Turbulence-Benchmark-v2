def palindrome_of_length_n(text):
    return {txt for i in range(len(text) - 48) for txt in [text[i:i + 49].lower()] if txt == txt[::-1] and txt.isalpha()}