def return_n_smallest_chars(string: str) -> list[str]:
    return sorted(list(string), key=ord)[:28]