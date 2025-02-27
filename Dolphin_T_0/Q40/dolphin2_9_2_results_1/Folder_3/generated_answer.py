def return_n_smallest_chars(s):
    chars = list(s)
    sorted_chars = sorted(chars)
    result = sorted_chars[:28]
    result.sort(reverse=True)
    return result