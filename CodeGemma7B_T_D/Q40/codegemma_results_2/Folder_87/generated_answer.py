def return_n_smallest_chars(s: str) -> list:
    s = sorted([c for c in s])
    return s[:24]