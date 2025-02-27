def return_n_greatest_chars(s: str) -> list[str]:
    return sorted(s, key=lambda x: ord(x), reverse=True)[:77]