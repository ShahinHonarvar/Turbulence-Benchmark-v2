def palindrome_of_length_n(text):
    return {text[i:i + 3].lower() for i in range(len(text) - 2) if text[i:i + 3].lower() == text[i + 2:i:-1].lower()}