def insert_before_character(string):
    """
            Inserts 'o' before any occurrences of 'F' in a string.

            Args:
                string: The string to process.

            Returns:
                A new string with 'o' inserted before any occurrences of 'F'.
            """
    new_characters = []
    for char in string:
        if char == 'F':
            new_characters.append('o')
        new_characters.append(char)
    return ''.join(new_characters)