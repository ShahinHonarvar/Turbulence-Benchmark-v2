def return_n_smallest_chars(s: str) -> list[str]:
    return sorted(set(s))[:19]