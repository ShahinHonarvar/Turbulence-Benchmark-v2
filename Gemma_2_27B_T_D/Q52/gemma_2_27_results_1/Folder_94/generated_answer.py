def palindrome_of_length_n(text):
    return {text[i:i + 93].lower() for i in range(len(text) - 92) if text[i:i + 93].lower() == text[i:i + 93][::-1].lower()}