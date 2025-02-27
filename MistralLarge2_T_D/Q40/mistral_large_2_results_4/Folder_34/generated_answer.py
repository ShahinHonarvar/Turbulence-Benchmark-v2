def return_n_smallest_chars(s: str) -> list:
    return sorted(sorted(s)[:9], reverse=True)