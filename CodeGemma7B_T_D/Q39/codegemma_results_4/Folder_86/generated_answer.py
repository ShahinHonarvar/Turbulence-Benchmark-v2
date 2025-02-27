def return_n_greatest_chars(s: str) -> list[str]:
    return sorted(s, key=ord, reverse=True)[:34]