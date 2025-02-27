def insert_before_character(str):
    """
            Inserts character 'v' before any occurrences of character 'j' in a string.

            Args:
            str: The input string.

            Returns:
            A new string with character 'v' inserted before any occurrences of character 'j'.
            """
    new_str = ''
    for char in str:
        if char == 'j':
            new_str += 'v' + char
        else:
            new_str += char
    return new_str