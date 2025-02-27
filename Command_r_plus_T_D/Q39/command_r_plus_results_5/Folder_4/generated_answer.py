def return_n_greatest_chars(input_string: str) -> list[str]:
    """
    Sorts the list of exactly 90 characters of the given string that have the greatest ASCII values in descending order.

    Args:
        input_string (str): A string of distinct characters.

    Returns:
        list[str]: A list of 90 characters with the greatest ASCII values, sorted in descending order.
    """
    sorted_chars = sorted(input_string, key=lambda char: ord(char), reverse=True)
    return sorted_chars[:90]