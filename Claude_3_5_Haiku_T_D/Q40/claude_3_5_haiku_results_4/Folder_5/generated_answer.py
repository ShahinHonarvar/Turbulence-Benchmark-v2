def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string), reverse=True)
    result = sorted_chars[:46] if len(sorted_chars) >= 46 else sorted_chars
    return result