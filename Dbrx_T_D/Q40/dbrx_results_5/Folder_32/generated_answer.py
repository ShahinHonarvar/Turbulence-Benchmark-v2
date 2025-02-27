def return_n_smallest_chars(s: str) -> list:
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[:8]