def palindrome_of_length_n(text):
    return {text[i:i + 47].lower() for i in range(len(text) - 46) if text[i:i + 47].lower() == text[i:i + 47][::-1].lower() and text[i:i + 47].isalpha()}