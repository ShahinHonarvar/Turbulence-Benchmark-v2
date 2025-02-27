def return_n_greatest_chars(input_string: str) -> list[str]:
    """
    Returns a list of 36 characters with the greatest ASCII values from the input string.

    Args:
        input_string (str): A string of distinct characters.

    Returns:
        list[str]: A list of 36 characters with the greatest ASCII values, sorted in descending order.
    """
    sorted_string = sorted(input_string, key=lambda char: ord(char), reverse=True)
    return sorted_string[:36]