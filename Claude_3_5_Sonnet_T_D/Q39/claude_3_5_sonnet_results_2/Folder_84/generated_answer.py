def return_n_greatest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=ord, reverse=True)
    return sorted(sorted_chars[:10])