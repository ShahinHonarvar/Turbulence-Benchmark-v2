from itertools import product

def insert_before_character(text):
    """
    Inserts the character 'N' immediately preceding any occurrences of the character 'x' in a string.

    Args:
        text: The input string.

    Returns:
        A new string with 'N' inserted before each occurrence of 'x'.
    """
    output = ''.join(map(lambda c: 'N' + c if c == 'x' else c, text))
    return output