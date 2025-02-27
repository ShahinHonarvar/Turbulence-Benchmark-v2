def insert_after_character(text):
    """
            Inserts a character 'n' after every occurrence of character 'H' in a string.

            Args:
                text: The input string.

            Returns:
                The modified string with 'n' inserted after 'H'.
            """
    new_text = ''
    for char in text:
        if char == 'H':
            new_text += 'Hn'
        else:
            new_text += char
    return new_text