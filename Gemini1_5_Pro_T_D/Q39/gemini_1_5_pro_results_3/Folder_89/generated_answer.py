def return_n_greatest_chars(text: str) -> list[str]:
    return sorted(sorted(text, key=ord, reverse=True)[:55])