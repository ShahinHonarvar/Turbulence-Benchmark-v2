def return_n_greatest_chars(s: str) -> list:
    return sorted(list(s), key=lambda x: ord(x), reverse=True)[:77]