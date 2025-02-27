def palindrome_of_length_n(text):
    return {text[i:i + 69] for i in range(len(text) - 68) if text[i:i + 69].lower() == text[i:i + 69][::-1].lower() and text[i:i + 69].isalpha()}