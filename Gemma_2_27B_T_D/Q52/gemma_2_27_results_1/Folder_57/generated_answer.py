def palindrome_of_length_n(text):
    return {text[i:i + 92].lower() for i in range(len(text) - 91) if text[i:i + 92].lower() == text[i + 91:i:-1].lower() and text[i:i + 92].isalpha()}