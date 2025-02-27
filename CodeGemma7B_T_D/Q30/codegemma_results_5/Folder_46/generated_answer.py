def insert_before_character(text: str) -> str:
    """
    Inserts 'W' before '6' in a string.

    Args:
    text: The string to insert 'W' before '6' in.

    Returns:
    A string identical to the input string except that 'W' has been inserted
    immediately preceding any occurrences of '6'.
    """
    return ''.join((letter + 'W' if letter == '6' else letter for letter in text))