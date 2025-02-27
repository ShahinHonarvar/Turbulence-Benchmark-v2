def palindrome_of_length_n(text):
    return {text[i:i + 42].lower() for i in range(len(text) - 41) if text[i:i + 42].lower() == text[i:i + 42][::-1].lower()}