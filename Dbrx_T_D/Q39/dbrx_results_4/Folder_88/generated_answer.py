def return_n_greatest_chars(s: str) -> list:
    return sorted(list(s), key=ord, reverse=True)[:84]