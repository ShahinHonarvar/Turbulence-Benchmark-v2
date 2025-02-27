def palindrome_of_length_n(text):
    return {text[i:i + 94] for i in range(len(text) - 93) if text[i:i + 94].lower() == text[i:i + 94][::-1].lower() and text[i:i + 94].isalpha()}