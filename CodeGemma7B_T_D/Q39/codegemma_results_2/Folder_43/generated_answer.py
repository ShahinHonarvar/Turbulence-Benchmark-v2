def return_n_greatest_chars(given_string):
    return sorted(given_string, key=ord, reverse=True)[:56]