def return_n_smallest_chars(string_of_chars):
    sorted_chars = sorted(list(set(string_of_chars)))
    return sorted_chars[:68][::-1]