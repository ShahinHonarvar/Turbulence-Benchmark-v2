def palindrome_of_length_n(text):
    return {text[i:i + 99].lower() for i in range(len(text) - 98) if text[i:i + 99].lower() == text[i:i + 99][::-1].lower() and text[i:i + 99].isalpha()}