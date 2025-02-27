def return_n_smallest_chars(s: str) -> list:
    return sorted([c for c in s if ord(c) < 123], reverse=True)[:90]