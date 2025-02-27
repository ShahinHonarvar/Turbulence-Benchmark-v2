def return_n_greatest_chars(s: str) -> list[str]:
    sorted_chars = sorted(s, reverse=True)
    return sorted_chars[:57]