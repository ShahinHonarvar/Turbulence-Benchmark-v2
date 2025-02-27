def return_n_smallest_chars(s: str) -> list:
    s = ''.join(sorted(s))
    return sorted(list(s[:46]))