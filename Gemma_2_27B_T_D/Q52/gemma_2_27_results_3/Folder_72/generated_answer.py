def palindrome_of_length_n(text):
    return {text[i:i + 16].lower() for i in range(len(text) - 15) if text[i:i + 16].lower() == text[i:i + 16][::-1].lower()}