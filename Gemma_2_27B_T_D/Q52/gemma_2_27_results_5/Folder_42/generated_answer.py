def palindrome_of_length_n(text):
    return set([text[i:i + 279].lower() for i in range(len(text) - 278) if text[i:i + 279].lower() == text[i:i + 279].lower()[::-1] and text[i:i + 279].isalpha()])