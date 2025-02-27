def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string, key=lambda x: -ord(x))
    return sorted([char for char in sorted_chars[:10]])