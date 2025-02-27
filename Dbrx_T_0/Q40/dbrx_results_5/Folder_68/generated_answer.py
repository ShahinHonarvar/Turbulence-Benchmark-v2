def return_n_smallest_chars(string_of_chars):
    sorted_chars = sorted(string_of_chars, key=ord)
    return sorted_chars[::-1][:89]