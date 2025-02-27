def return_nth_smallest_ascii(strg):
    """
            Returns the character with the 20th smallest ASCII value among those characters in the string that occur between indices 10 to 90, both inclusive.
            """
    strg = strg[10:91]
    ascii_values = sorted([ord(char) for char in strg])
    return chr(ascii_values[19])