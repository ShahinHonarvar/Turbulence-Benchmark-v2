def insert_before_character(text):
    """Given a text, this function inserts a character before specific characters in the text.

            Args:
                text: The text to insert the character before.

            Returns:
                The text with the character inserted before specific characters.
            """
    return ''.join([char + '9' if char == '6' else char for char in text])