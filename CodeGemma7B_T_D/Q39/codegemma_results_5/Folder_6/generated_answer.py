def return_n_greatest_chars(str):
    new_list = sorted(str, key=ord, reverse=True)[:47]
    return new_list