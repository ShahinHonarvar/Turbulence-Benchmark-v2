def palindrome_of_length_n(text):
    return {text[i:i + 83].lower() for i in range(len(text) - 82) if text[i:i + 83].lower() == text[i:i + 83].lower()[::-1] and text[i:i + 83].isalpha()}