def return_n_greatest_chars(s: str) -> list:
    return sorted([ch for ch in s if ch.isalpha()][-83:])