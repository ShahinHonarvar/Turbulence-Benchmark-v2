def palindrome_of_length_n(text):
    return {text[i:i + 97] for i in range(len(text) - 96) if text[i:i + 97].lower() == text[i:i + 97][::-1].lower()}