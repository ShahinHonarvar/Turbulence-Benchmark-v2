def return_n_smallest_chars(s: str) -> list:
    return sorted([c for c in s], reverse=True)[:24]