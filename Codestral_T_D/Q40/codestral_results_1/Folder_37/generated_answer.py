def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)[:26]
    sorted_chars.reverse()
    return sorted_chars