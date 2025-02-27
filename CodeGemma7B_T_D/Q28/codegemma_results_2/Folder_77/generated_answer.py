def return_nth_smallest_ascii(s):
    """
            Returns the character with the 14th smallest ASCII value among those characters in the string that occur between indices 63 to 76, both inclusive.
            """
    sorted_chars = sorted(s[63:77])
    return sorted_chars[13]