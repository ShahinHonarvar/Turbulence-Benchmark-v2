def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    result = sorted_chars[:72]
    return sorted(result, reverse=True)