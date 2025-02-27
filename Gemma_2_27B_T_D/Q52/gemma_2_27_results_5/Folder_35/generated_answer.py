def palindrome_of_length_n(text):
    return {text[i:i + 116].lower() for i in range(len(text) - 115) if text[i:i + 116].lower() == text[i:i + 116].lower()[::-1] and text[i:i + 116].isalpha()}