def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    result = sorted_chars[:60]
    while len(result) < 60:
        result.append(max(sorted_chars))
    return result