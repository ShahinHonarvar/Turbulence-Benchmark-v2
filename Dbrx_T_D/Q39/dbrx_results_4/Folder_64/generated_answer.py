def return_n_greatest_chars(s: str) -> list[str]:
    return sorted(list(set(s)), reverse=True)[:39]