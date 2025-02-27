def return_n_smallest_chars(input_str):
    return sorted([char for char in input_str], key=lambda x: ord(x), reverse=True)[:56]