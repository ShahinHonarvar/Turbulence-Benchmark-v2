def palindrome_of_length_n(text):
    return {text[i:i + 90].lower() for i in range(len(text) - 89) if text[i:i + 90].lower() == text[i + 89:i:-1].lower()}