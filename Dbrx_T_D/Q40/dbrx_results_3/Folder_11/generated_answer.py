def return_n_smallest_chars(s: str) -> list:
    return sorted(list(set(s)))[:17]