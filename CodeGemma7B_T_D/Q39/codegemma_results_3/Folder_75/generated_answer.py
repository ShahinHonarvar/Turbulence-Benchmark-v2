def return_n_greatest_chars(str):
    new_str = sorted(str, key=ord, reverse=True)
    return new_str[:2]