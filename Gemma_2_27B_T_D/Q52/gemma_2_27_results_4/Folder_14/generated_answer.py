def palindrome_of_length_n(text):
    return {text[i:i + 63].lower() for i in range(len(text) - 62) if text[i:i + 63].lower() == text[i:i + 63][::-1].lower() and text[i:i + 63].isalpha()}