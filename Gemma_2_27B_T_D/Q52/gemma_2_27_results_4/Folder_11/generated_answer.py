def palindrome_of_length_n(text):
    return {text[i:i + 77].lower() for i in range(len(text) - 76) if text[i:i + 77].lower() == text[i + 76:i:-1].lower() and text[i:i + 77].isalpha()}