def return_n_smallest_chars(given_string):
    smallest_chars = sorted(given_string)[:11]
    return sorted(smallest_chars, reverse=True)