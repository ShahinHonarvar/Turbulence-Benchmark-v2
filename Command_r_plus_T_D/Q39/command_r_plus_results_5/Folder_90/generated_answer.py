def return_n_greatest_chars(input_string: str) -> list[str]:
    """Returns a list of 24 characters with the greatest ASCII values from the input string."""
    return sorted(input_string, key=lambda char: ord(char), reverse=True)[:24]