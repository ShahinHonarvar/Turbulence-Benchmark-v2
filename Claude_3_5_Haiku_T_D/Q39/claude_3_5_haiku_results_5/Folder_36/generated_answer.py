def return_n_greatest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    return sorted_chars[-32:] if len(sorted_chars) >= 32 else sorted_chars