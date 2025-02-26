def return_n_greatest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x), reverse=True)
    return sorted_chars[:36]