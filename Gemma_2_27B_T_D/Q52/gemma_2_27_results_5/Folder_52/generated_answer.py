def palindrome_of_length_n(text):
    return {text[i:i + 423] for i in range(len(text) - 422) if text[i:i + 423].lower() == text[i:i + 423][::-1].lower()}