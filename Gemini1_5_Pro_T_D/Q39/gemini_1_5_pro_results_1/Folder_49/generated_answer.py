def return_n_greatest_chars(text):
    return sorted([char for char in text if ord(char) >= 32 and ord(char) <= 126], key=ord, reverse=True)[:76]