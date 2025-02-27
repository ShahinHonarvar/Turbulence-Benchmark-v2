def return_n_smallest_chars(s: str) -> list:
    ascii_sorted = sorted(s, key=ord)
    return ascii_sorted[:23]