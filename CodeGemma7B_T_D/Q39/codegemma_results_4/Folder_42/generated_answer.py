def return_n_greatest_chars(given_str):
    ascii_values = [ord(char) for char in given_str]
    ascii_values.sort(reverse=True)
    return ascii_values[:59]