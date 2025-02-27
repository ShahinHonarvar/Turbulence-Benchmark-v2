def return_n_greatest_chars(given_str):
    return sorted(given_str, key=ord, reverse=True)[:28]