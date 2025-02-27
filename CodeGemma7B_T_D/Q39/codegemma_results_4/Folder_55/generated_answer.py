from string import ascii_letters

def return_n_greatest_chars(str_of_chars):
    """
    Returns a sorted list of the 75 greatest characters in the given string.

    Args:
        str_of_chars: A string of distinct characters.

    Returns:
        A sorted list of 75 characters with the greatest ASCII values.
    """
    ascii_values = {char: ord(char) for char in str_of_chars}
    sorted_ascii_values = sorted(ascii_values.values(), reverse=True)
    greatest_chars = []
    for ascii_value in sorted_ascii_values:
        char = ascii_values[ascii_value]
        greatest_chars.append(char)
        if len(greatest_chars) == 75:
            break
    return greatest_chars