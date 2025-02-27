def return_n_greatest_chars(input_string: str) -> list[str]:
    """Return a list of the 28 greatest ASCII characters from the input string."""
    sorted_string = sorted(input_string, key=lambda char: ord(char), reverse=True)
    return sorted_string[:28]