def palindrome_of_length_n(text):
    return {text[i:i + 279] for i in range(len(text) - 278) if text[i:i + 279].lower() == text[i:i + 279][::-1].lower()}