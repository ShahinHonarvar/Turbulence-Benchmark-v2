def return_n_greatest_chars(text):
    return sorted([char for char in text if ord(char) > 0], key=ord, reverse=True)[:87]