def palindrome_of_length_n(text):
    return {text[i:i + 21].lower() for i in range(len(text) - 20) if text[i:i + 21].lower() == text[i + 20:i:-1].lower() and text[i:i + 21].isalpha()}