def return_n_greatest_chars(input_string: str) -> list[str]:
    sorted_chars = sorted(input_string, reverse=True)
    greatest_83_chars = sorted_chars[:83]
    return greatest_83_chars