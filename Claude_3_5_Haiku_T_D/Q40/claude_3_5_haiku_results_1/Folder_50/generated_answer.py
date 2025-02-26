def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))[:16]
    sorted_chars.sort(reverse=True)
    return sorted_chars