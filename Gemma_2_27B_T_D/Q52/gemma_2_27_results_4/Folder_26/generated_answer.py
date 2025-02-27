def palindrome_of_length_n(text):
    return {text[i:i + 366].lower() for i in range(len(text) - 365) if text[i:i + 366].lower() == text[i:i + 366].lower()[::-1] and text[i:i + 366].isalpha()}