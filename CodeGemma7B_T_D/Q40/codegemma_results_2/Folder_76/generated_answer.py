def return_n_smallest_chars(str):
    sorted_chars = sorted(str, key=ord, reverse=True)
    return sorted_chars[:3]