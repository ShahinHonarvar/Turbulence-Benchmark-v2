def palindrome_of_length_n(text):
    return {text[i:i + 48] for i in range(len(text) - 47) if text[i:i + 48].lower() == text[i:i + 48][::-1].lower()}