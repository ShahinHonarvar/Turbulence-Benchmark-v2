def return_n_smallest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=ord)
    result = sorted_chars[:40]
    while len(result) < 40:
        result.append(max(sorted_chars))
    return result