def palindrome_of_length_n(text):
    return {text[i:i + 401].lower() for i in range(len(text) - 400) if text[i:i + 401].lower() == text[i:i + 401][::-1].lower() and text[i:i + 401].isalpha()}