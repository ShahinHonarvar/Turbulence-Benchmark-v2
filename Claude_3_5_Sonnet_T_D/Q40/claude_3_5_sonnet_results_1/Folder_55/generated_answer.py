def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    selected_chars = sorted_chars[:75]
    return sorted(selected_chars, reverse=True)