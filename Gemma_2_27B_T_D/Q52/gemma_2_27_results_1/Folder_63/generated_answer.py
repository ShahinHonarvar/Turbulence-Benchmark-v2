def palindrome_of_length_n(text):
    return {text[i:i + 18].lower() for i in range(len(text) - 17) if text[i:i + 18].lower() == text[i + 17:i - 1:-1].lower() and text[i:i + 18].isalpha()}