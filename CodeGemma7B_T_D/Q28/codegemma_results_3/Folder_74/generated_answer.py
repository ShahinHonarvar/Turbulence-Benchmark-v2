def return_nth_smallest_ascii(txt):
    """
            Returns the character with the 6th smallest ASCII value among those characters in the string that occur between indices 1 to 31, both inclusive.

            Args:
            txt: A string of distinct characters.

            Returns:
            The character with the 6th smallest ASCII value.
            """
    char_list = list(txt)
    ascii_values = {}
    for i, char in enumerate(char_list):
        if 1 <= i <= 31:
            ascii_values[char] = ord(char)
    sorted_values = sorted(ascii_values.values())
    return chr(sorted_values[5])