def return_n_greatest_chars(input_string: str) -> list[str]:
    sorted_string = sorted(input_string, reverse=True)
    return sorted_string[:27]