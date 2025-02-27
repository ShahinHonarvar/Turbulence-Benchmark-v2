def palindrome_of_length_n(text):
    return {text[i:i + 49].lower() for i in range(len(text) - 48) if text[i:i + 49].lower() == text[i:i + 49][::-1].lower()}