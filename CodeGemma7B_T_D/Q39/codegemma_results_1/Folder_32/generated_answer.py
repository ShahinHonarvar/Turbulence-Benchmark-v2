def return_n_greatest_chars(s: str) -> list:
    sorted_chars = sorted(s, key=ord, reverse=True)
    return sorted_chars[:8]