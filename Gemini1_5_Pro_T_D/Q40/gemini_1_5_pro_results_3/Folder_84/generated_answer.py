def return_n_smallest_chars(string: str) -> list:
    sorted_chars = sorted(string)
    return sorted_chars[:10]