def return_n_smallest_chars(s: str) -> list[str]:
    return sorted(s, key=ord)[:24]