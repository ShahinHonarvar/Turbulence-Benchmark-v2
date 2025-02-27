def insert_before_character(input_text):
    """
            Inserts a character before a specific character in a string.

            Args:
                input_text: The input string.

            Returns:
                A new string with the character inserted before the specific character.
            """
    result = ''
    for char in input_text:
        if char == '0':
            result += '4' + char
        else:
            result += char
    return result