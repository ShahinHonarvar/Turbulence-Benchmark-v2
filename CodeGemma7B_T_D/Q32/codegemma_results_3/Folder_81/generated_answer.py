def insert_after_character(text):
    """Inserts 'A' after 'A' in a string.

            Args:
                text: The string to insert 'A' into.

            Returns:
                The string with 'A' inserted after 'A'.
            """
    new = ''
    for char in text:
        if char == 'A':
            new += char + 'A'
        else:
            new += char
    return new