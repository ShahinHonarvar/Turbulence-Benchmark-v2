def palindrome_of_length_n(text):
    return {text[i:i + 80] for i in range(len(text) - 79) if text[i:i + 80].lower() == text[i:i + 80][::-1].lower() and text[i:i + 80].isalpha()}