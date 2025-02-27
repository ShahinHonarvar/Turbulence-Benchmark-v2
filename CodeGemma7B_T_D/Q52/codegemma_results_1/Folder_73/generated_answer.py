def palindrome_of_length_n(text):
    return set([text[i:j + 1] for i in range(len(text) - 40) for j in range(i, len(text)) if text[i:j + 1] == text[i:j + 1][::-1] and text[i:j + 1].isalpha()])