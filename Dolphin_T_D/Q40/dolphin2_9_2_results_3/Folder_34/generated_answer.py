def return_n_smallest_chars(input_str):
    return sorted([char for char in input_str], reverse=True)[:9]