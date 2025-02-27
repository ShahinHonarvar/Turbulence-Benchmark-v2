def palindrome_of_length_n(text):
    return {text[i:i + 338] for i in range(len(text) - 337) if text[i:i + 338].lower() == text[i + 337:i:-1].lower()}