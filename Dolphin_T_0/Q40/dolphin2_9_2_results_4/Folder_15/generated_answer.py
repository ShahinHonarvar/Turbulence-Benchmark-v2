def return_n_smallest_chars(inputs):
    sorted_chars = sorted(inputs, key=lambda x: ord(x))
    return sorted_chars[:57]