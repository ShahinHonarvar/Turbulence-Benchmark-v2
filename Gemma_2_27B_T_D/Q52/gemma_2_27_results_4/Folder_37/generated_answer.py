def palindrome_of_length_n(text):
    return {text[i:i + 84].lower() for i in range(len(text) - 83) if text[i:i + 84].lower() == text[i:i + 84].lower()[::-1] and text[i:i + 84].isalpha()}