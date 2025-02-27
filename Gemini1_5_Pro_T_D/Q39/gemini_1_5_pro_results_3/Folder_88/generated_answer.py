def return_n_greatest_chars(s: str) -> list:
    return sorted([c for c in sorted(s, reverse=True)[:84]])