def return_n_smallest_chars(input_string):
    distinct_chars = list(set(input_string))
    sorted_chars = sorted(distinct_chars, key=ord)
    smallest_chars = sorted_chars[:72]
    smallest_chars.extend([chr(0)] * (72 - len(smallest_chars)))
    return sorted(smallest_chars, reverse=True)