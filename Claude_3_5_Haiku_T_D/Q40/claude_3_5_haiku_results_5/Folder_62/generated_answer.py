def return_n_smallest_chars(input_string):
    sorted_chars = sorted(list(input_string))
    result = sorted_chars[:84] if len(sorted_chars) >= 84 else sorted_chars
    return sorted(result, reverse=True)