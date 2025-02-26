def return_n_smallest_chars(input_string):
    distinct_chars = list(set(input_string))
    sorted_chars = sorted(distinct_chars, key=ord)
    result = sorted_chars[:60]
    while len(result) < 60:
        result.extend(result[:60 - len(result)])
    return result[:60]