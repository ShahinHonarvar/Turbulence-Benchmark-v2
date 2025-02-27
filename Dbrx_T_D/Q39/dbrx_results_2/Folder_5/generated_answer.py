def return_n_greatest_chars(s: str) -> str:
    return sorted(s, key=ord, reverse=True)[:46]