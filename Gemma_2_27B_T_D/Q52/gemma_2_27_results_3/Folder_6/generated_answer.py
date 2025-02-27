def palindrome_of_length_n(text):
    return {text[i:i + 474].lower() for i in range(len(text) - 473) if text[i:i + 474].lower() == text[i:i + 474][::-1].lower()}