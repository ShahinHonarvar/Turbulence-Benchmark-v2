def palindrome_of_length_n(text):
    return {text[i:i + 113].lower() for i in range(len(text) - 112) if text[i:i + 113].lower() == text[i:i + 113][::-1].lower() and text[i:i + 113].isalpha()}