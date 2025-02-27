def return_n_greatest_chars(given_string):
    sorted_chars = sorted(given_string)
    return sorted_chars[-24:][::-1]