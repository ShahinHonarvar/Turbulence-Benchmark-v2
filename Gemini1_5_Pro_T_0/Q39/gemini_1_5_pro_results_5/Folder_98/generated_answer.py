def return_n_greatest_chars(text):
    return sorted([char for char in text if ord(char) >= ord(sorted(text)[len(text) - 68])], key=ord, reverse=True)