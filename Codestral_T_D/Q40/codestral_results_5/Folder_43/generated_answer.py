def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    smallest_chars = sorted_chars[:56]
    smallest_chars.sort(reverse=True)
    return smallest_chars