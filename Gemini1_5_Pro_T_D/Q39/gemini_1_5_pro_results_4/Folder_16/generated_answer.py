def return_n_greatest_chars(text: str) -> list[str]:
    return sorted([*text], reverse=True)[:64]