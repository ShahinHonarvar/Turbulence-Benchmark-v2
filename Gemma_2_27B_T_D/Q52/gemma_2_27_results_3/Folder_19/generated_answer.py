def palindrome_of_length_n(text):
    return {text[i:i + 67].lower() for i in range(len(text) - 66) if text[i:i + 67].lower() == text[i + 66:i:-1].lower()}