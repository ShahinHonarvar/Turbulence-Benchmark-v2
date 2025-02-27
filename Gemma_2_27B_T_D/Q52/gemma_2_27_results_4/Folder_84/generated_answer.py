def palindrome_of_length_n(text):
    return {text[i:i + 131] for i in range(len(text) - 130) if text[i:i + 131].lower() == text[i:i + 131][::-1].lower() and text[i:i + 131].isalpha()}