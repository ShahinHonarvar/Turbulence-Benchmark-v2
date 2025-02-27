def return_n_greatest_chars(input_string):
    """
    This function takes one argument, a string of distinct characters and creates the sorted list of exactly 46 characters of the given string that have the greatest ASCII values. The function sorts them in descending order and returns them.

    Args:
    input_string: A string of distinct characters.

    Returns:
    A list of 46 characters sorted in descending order.
    """
    chars = list(input_string)
    if len(chars) < 46:
        return 'Error: Input string needs to contain at least 46 distinct characters.'
    sorted_chars = sorted(chars, key=lambda c: -ord(c))
    return sorted_chars[:46]