def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    smallest_37 = sorted_chars[:37]
    return sorted(smallest_37, reverse=True)