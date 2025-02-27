def return_n_smallest_chars(given_string):
    return sorted(given_string, key=ord, reverse=True)