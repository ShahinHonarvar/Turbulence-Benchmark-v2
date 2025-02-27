def palindrome_of_length_n(text):
    return {text[i:i + 223].lower() for i in range(len(text) - 222) if text[i:i + 223].lower() == text[i:i + 223].lower()[::-1] and text[i:i + 223].isalpha()}