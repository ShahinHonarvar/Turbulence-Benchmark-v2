def insert_after_character(text):
    """Inserts the character 'P' immediately following each space in the given text.

            Args:
                text: The input text.

            Returns:
                A string with 'P' inserted after each space.
            """
    new_text = []
    for char in text:
        if char == ' ':
            new_text.append(char)
            new_text.append('P')
        else:
            new_text.append(char)
    return ''.join(new_text)