def return_n_smallest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=ord)
    result = sorted_chars[:80]
    while len(result) < 80:
        result.extend(sorted_chars[:80 - len(result)])
    return result