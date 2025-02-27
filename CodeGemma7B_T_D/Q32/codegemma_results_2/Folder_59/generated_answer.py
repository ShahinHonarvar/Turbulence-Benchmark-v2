def insert_after_character(old_string):
    """
    Inserts '0' after every 'o' in a string.

    Args:
        old_string: The string to insert '0' after 'o' in.

    Returns:
        A new string with '0' inserted after every 'o'.
    """
    new_string = ''
    for char in old_string:
        if char == 'o':
            new_string += char + '0'
        else:
            new_string += char
    return new_string