def return_n_smallest_chars(input_string):
    unique_chars = set(input_string)
    sorted_chars = sorted(unique_chars, key=ord)
    result = sorted_chars[:72]
    while len(result) < 72:
        result.extend(result[:72 - len(result)])
    return result