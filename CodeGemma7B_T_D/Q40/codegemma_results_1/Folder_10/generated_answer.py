def return_n_smallest_chars(str):
    result = sorted(str, key=ord, reverse=False)
    result = result[:88]
    return result