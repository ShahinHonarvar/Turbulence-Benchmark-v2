def return_n_greatest_chars(s: str) -> list[str]:
    return sorted(s, reverse=True)[:49]