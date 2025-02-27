def insert_before_character(string):
    """Inserts character 'P' before any occurrences of character ' ' in a string.

            Args:
                string: The input string.

            Returns:
                The output string with 'P' inserted before any occurrences of ' '.
            """
    output_string = ''
    for char in string:
        if char == ' ':
            output_string += 'P '
        else:
            output_string += char
    return output_string