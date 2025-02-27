def palindrome_of_length_n(text):
    return {text[i:i + 276].lower() for i in range(len(text) - 275) if text[i:i + 276].lower() == text[i:i + 276].lower()[::-1] and text[i:i + 276].isalpha()}