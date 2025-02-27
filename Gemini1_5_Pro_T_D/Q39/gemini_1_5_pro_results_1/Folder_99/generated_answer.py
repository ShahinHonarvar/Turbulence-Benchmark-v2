def return_n_greatest_chars(text):
    return sorted([char for char in text if ord(char) >= ord(sorted(text)[-35])], reverse=True)