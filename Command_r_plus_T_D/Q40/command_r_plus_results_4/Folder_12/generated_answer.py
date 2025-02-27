def return_n_smallest_chars(s: str) -> list[str]:
    sorted_s = sorted(s, reverse=True)
    return sorted_s[:61]