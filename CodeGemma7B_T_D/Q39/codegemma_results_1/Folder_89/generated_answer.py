def return_n_greatest_chars(str):
    return sorted(str, key=ord, reverse=True)[:55]