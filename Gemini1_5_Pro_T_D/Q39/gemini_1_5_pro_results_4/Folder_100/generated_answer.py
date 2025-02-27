def return_n_greatest_chars(text):
    return sorted([char for char in text if ord(char) <= 126], reverse=True)[:72]