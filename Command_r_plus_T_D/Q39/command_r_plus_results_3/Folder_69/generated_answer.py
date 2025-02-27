def return_n_greatest_chars(input_string: str) -> list[str]:
    """
    Sorts the given string in descending order and returns a list of 65 characters with the greatest ASCII values.

    Args:
        input_string (str): A string of distinct characters.

    Returns:
        list[str]: A list of 65 characters with the greatest ASCII values.
    """
    sorted_string = sorted(input_string, reverse=True)
    return sorted_string[:65]