def palindrome_of_length_at_least_n(text):
    distinctlist = set([text[i:j + 1] for i in range(len(text)) for j in range(i + 1, len(text)) if text[i:j + 1].isalpha() and text[i:j + 1] == text[i:j + 1][::-1]])
    return distinctlist