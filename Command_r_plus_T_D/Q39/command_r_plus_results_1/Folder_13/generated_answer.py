def return_n_greatest_chars(input_string: str) -> list[str]:
    """
    Sorts and returns a list of 31 characters from the input string with the greatest ASCII values.

    Args:
        input_string (str): A string of distinct characters.

    Returns:
        list[str]: A sorted list of 31 characters with the greatest ASCII values.
    """
    sorted_chars = sorted(input_string, reverse=True)
    return sorted_chars[:31]