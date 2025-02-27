def return_n_greatest_chars(text: str) -> list[str]:
    sorted_chars = sorted(text, reverse=True)
    return sorted_chars[:84]