def return_n_smallest_chars(string):
    unique_chars = list(set(string))
    sorted_chars = sorted(unique_chars)
    result = sorted_chars[:16]
    result.sort(reverse=True)
    return result