def return_n_smallest_chars(chars: str) -> list[str]:
    chars = sorted(chars, key=ord)
    return chars[:12]