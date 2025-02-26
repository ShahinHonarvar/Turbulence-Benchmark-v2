def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    smallest_three = sorted_chars[:3]
    return sorted(smallest_three, reverse=True)