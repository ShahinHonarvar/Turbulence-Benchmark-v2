def return_n_greatest_chars(input_str: str) -> list[str]:
    sorted_chars = sorted(input_str, reverse=True)
    return sorted_chars[:49]