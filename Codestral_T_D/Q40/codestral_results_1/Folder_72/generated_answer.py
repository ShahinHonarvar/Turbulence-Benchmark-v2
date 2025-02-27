def return_n_smallest_chars(s):
    if len(s) < 37:
        raise ValueError('Input string must have at least 37 distinct characters')
    sorted_chars = sorted(s)
    return sorted_chars[:37][::-1]