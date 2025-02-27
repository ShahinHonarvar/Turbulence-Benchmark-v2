def return_n_greatest_chars(given_string):
    return sorted(given_string, key=str.ascii_value)[-23:]