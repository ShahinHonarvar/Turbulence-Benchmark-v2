def palindrome_of_length_n(text):
    return {text[i:i + 27].lower() for i in range(len(text) - 26) if text[i:i + 27].lower() == text[i:i + 27][::-1].lower() and text[i:i + 27].isalpha()}