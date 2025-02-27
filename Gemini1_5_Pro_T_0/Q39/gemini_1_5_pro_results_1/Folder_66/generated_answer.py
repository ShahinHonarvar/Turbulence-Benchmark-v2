def return_n_greatest_chars(text: str) -> list[str]:
    return sorted([c for c in text], reverse=True)[:33]