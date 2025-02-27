def return_n_greatest_chars(chars):
    """Return the greatest n characters in a string.

    Args:
        chars (str): A string of distinct characters.

    Returns:
        list: A sorted list of the greatest n characters in the string.
    """
    char_ascii_values = [(char, ord(char)) for char in chars]
    char_ascii_values.sort(key=lambda char_value: char_value[1], reverse=True)
    return char_ascii_values[:10]