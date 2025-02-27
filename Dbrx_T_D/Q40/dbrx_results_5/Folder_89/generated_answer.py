def return_n_smallest_chars(string_of_chars):
    sorted_chars = sorted(list(set(string_of_chars)))[:55]
    return sorted_chars