def palindrome_of_length_n(text):
    return {text[i:i + 78].lower() for i in range(len(text) - 77) if text[i:i + 78].lower() == text[i:i + 78][::-1].lower()}