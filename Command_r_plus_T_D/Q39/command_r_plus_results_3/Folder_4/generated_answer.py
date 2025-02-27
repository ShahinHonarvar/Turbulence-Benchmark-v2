def return_n_greatest_chars(input_string: str) -> list[str]:
    """Sorts and returns a list of 90 characters with the greatest ASCII values."""
    sorted_chars = sorted(input_string, reverse=True)
    return sorted_chars[:90]