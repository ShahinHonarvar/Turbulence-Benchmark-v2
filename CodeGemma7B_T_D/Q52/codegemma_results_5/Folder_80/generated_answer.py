def palindrome_of_length_n(text):
    text = text.lower()
    return {text[i:i + 276] for i in range(len(text) - 276 + 1) if text[i:i + 276].isalpha()}