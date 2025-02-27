def return_n_greatest_chars(string: str) -> list[str]:
    sorted_chars = sorted(string, reverse=True)
    return sorted_chars[:33]