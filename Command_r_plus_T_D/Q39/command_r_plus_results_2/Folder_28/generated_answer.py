def return_n_greatest_chars(input_string: str) -> list[str]:
    """
    Sorts the list of characters in the input string based on their ASCII values in ascending order,
    and returns a list of the 3 characters with the greatest ASCII values.

    Parameters:
    input_string (str): A string of distinct characters.

    Returns:
    list[str]: A list of exactly 3 characters with the greatest ASCII values in ascending order.
    """
    sorted_string = sorted(input_string, key=lambda char: ord(char), reverse=True)
    return sorted_string[:3]