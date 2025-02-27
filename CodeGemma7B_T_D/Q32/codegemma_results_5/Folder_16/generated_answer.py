def insert_after_character(str):
    """
            Inserts character 'n' immediately succeeding any occurrences of character 'w' in a string.

            Args:
                str: The string to insert the character into.

            Returns:
                The string with 'n' inserted after every 'w'.
            """
    new_str = ''
    for char in str:
        if char == 'w':
            new_str += char + 'n'
        else:
            new_str += char
    return new_str