def return_n_smallest_chars(s: str) -> list[str]:
    return sorted(s, key=lambda x: ord(x))[:35]