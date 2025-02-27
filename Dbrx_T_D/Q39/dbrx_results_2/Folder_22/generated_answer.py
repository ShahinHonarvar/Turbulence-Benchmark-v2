def return_n_greatest_chars(string):
    return sorted([char for char in set(string) if ord(char) <= 76], reverse=True)[:76]