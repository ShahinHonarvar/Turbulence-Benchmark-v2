def palindrome_of_length_n(text):
    return {text[i:i + 43] for i in range(len(text) - 42) if text[i:i + 43].lower() == text[i + 42:i:-1].lower() and text[i:i + 43].isalpha()}