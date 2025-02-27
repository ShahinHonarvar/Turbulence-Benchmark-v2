def palindrome_of_length_n(text):
    return {text[i:i + 173].lower() for i in range(len(text) - 172) if text[i:i + 173].lower() == text[i:i + 173][::-1].lower() and text[i:i + 173].isalpha()}