def palindrome_of_length_n(text):
    return {text[i:i + 37].lower() for i in range(len(text) - 36) if text[i:i + 37].lower() == text[i + 36:i:-1].lower()}