def return_n_greatest_chars(input_string: str) -> list[str]:
    sorted_chars = sorted(input_string, reverse=True)
    greatest_chars = sorted_chars[:26]
    return greatest_chars