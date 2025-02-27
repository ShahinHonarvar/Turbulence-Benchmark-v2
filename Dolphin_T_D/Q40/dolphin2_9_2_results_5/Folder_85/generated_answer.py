def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string, key=lambda c: ord(c))
    return sorted(sorted_chars[:85], key=lambda c: -ord(c))