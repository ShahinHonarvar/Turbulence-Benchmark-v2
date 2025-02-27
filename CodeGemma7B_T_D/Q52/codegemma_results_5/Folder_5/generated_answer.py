def palindrome_of_length_n(text):
    return {text[i:i + 17].lower(): text[i:i + 17] for i in range(len(text) - 16) if text[i:i + 17].lower().isalpha()}