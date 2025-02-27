def return_n_smallest_chars(given_string):
    sorted_list = sorted(given_string, key=ord)
    return sorted_list[:68]