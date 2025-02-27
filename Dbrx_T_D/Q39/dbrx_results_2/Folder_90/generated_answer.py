def return_n_greatest_chars(text: str) -> list[str]:
    unique_chars = list(sorted(set(text), reverse=True))
    return unique_chars[:24] if len(unique_chars) >= 24 else unique_chars