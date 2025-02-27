def return_n_greatest_chars(input_string: str) -> list[str]:
    """
    Sorts and returns a list of exactly 27 characters from the input string with the greatest ASCII values.

    Args:
        input_string (str): A string of distinct characters.

    Returns:
        list[str]: A sorted list of 27 characters with the greatest ASCII values in descending order.
    """
    sorted_string = sorted(input_string, reverse=True)
    return sorted_string[:27]