def return_n_greatest_chars(input_string: str) -> list[str]:
    sorted_string = sorted(input_string, reverse=True)
    greatest_chars = sorted_string[:69]
    return greatest_chars