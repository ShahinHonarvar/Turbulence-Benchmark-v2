def return_n_greatest_chars(s: str) -> list[str]:
    return sorted(list(set(s)), key=ord, reverse=True)[:10]