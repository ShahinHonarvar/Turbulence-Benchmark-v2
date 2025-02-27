def return_n_greatest_chars(text: str) -> list[str]:
    sorted_chars = sorted(text, reverse=True)
    return sorted(sorted_chars[:69])