def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    result = sorted_chars[:79] if len(sorted_chars) >= 79 else sorted_chars + [chr(0)] * (79 - len(sorted_chars))
    return sorted(result, reverse=True)