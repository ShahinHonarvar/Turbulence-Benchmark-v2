def return_n_greatest_chars(input_string: str) -> list[str]:
    sorted_chars = sorted(input_string, reverse=True)
    return sorted_chars[:47]