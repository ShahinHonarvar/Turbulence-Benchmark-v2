def return_n_smallest_chars(s: str) -> list:
    sorted_chars = sorted(s)
    return sorted(sorted_chars[:77], reverse=True)