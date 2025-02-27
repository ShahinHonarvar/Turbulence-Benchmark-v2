def insert_after_character(text):
    """Inserts the character 'y' immediately succeeding any occurrences of the character 'b' in a string.

    Args:
      text: The input string.

    Returns:
      A string with 'y' inserted after each occurrence of 'b'.
    """
    return ''.join([char + 'y' if char == 'b' else char for char in text])