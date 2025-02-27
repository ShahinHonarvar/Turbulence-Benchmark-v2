def return_n_greatest_chars(s: str) -> list:
    return sorted(s, key=ord, reverse=True)[:13]