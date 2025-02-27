def return_n_smallest_chars(input_str: str) -> list[str]:
    smallest_chars = sorted(input_str, key=ord)[:66]
    return smallest_chars