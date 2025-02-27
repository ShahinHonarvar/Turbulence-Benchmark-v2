import string

def return_n_smallest_chars(chars):
    """
            This function returns a list of the 16 smallest characters in a string,
            sorted in descending order of ASCII value.

            Args:
                chars: A string of distinct characters.

            Returns:
                A list of 16 characters sorted in descending order of ASCII value.
            """
    if not chars:
        return []
    ascii_values = {c: ord(c) for c in chars}
    sorted_chars = sorted(ascii_values, key=ascii_values.get)
    return sorted_chars[:16]