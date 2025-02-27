def return_n_greatest_chars(input_str: str) -> list[str]:
    sorted_str = sorted(input_str, reverse=True)
    return sorted_str[:9]