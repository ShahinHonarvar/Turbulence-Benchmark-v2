def return_n_greatest_chars(input_string: str) -> list[str]:
    """
    Sorts and returns a list of 48 characters from the input string with the greatest ASCII values.

    Args:
        input_string (str): A string of distinct characters.

    Returns:
        list[str]: A list of 48 characters with the greatest ASCII values, sorted in ascending order.
    """
    sorted_string = sorted(input_string, key=lambda char: ord(char), reverse=True)
    return sorted_string[:48]