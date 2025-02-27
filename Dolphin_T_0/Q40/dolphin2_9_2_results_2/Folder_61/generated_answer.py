def return_n_smallest_chars(input_str):
    return sorted(list(input_str), key=lambda x: ord(x))[:66][::-1]