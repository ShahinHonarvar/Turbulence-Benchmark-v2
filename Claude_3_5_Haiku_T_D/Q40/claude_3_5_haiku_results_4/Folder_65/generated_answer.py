def return_n_smallest_chars(input_string):
    sorted_chars = sorted(list(set(input_string)))[:27]
    sorted_chars.sort(reverse=True)
    return sorted_chars