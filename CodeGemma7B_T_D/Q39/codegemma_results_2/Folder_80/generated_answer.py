def return_n_greatest_chars(str_distinct):
    """
    Returns a sorted list of 35 distinct characters from the given string of
    distinct characters with the greatest ASCII values.

    Args:
        str_distinct: A string of distinct characters.

    Returns:
        A sorted list of 35 distinct characters.
    """
    char_values = [(char, ord(char)) for char in str_distinct]
    char_values.sort(key=lambda x: x[1], reverse=True)
    return [char for char, _ in char_values[:35]]