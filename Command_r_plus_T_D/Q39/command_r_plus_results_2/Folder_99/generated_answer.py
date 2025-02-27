def return_n_greatest_chars(input_str: str) -> list[str]:
    return sorted(input_str, reverse=True)[:35]