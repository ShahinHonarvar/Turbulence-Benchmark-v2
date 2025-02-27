def palindrome_of_length_n(text):
    return {text[i:i + 472] for i in range(len(text) - 471) if text[i:i + 472].lower() == text[i:i + 472][::-1].lower() and text[i:i + 472].isalpha()}