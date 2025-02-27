def palindrome_of_length_n(text):
    return {text[i:i + 94].lower() for i in range(len(text) - 93) if text[i:i + 94].lower() == text[i + 93:i:-1].lower()}