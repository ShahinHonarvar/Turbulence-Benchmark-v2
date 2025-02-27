def palindrome_of_length_n(text):
    return {text[i:i + 464].lower() for i in range(len(text) - 463) if text[i:i + 464].lower() == text[i:i + 464][::-1].lower() and text[i:i + 464].isalpha()}