def return_n_greatest_chars(input_string: str) -> list[str]:
    sorted_string = sorted(input_string)
    greatest_chars = sorted_string[-43:]
    return greatest_chars