def return_n_greatest_chars(text: str) -> list[str]:
    sorted_chars = sorted(text, key=ord)
    return sorted_chars[-32:]