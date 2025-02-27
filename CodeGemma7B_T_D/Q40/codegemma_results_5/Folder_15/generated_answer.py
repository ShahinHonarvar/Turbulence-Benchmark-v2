def return_n_smallest_chars(str):
    sorted_str = sorted(str, key=ord)
    return sorted_str[:57]