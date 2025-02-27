def palindrome_of_length_n(text):
    return {text[i:i + 40].lower() for i in range(len(text) - 39) if text[i:i + 40].lower() == text[i + 39:i - 1:-1].lower() and text[i:i + 40].isalpha()}