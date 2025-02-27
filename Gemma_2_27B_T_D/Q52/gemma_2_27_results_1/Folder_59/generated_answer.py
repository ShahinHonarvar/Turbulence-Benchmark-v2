def palindrome_of_length_n(text):
    return {text[i:i + 39].lower() for i in range(len(text) - 38) if text[i:i + 39].lower() == text[i + 38:i:-1].lower() and text[i:i + 39].isalpha()}