def palindrome_of_length_n(text):
    return {text[i:i + 100].lower() for i in range(len(text) - 99) if text[i:i + 100].lower() == text[i:i + 100].lower()[::-1] and text[i:i + 100].isalpha()}