def return_nth_smallest_ascii(s):
    """Function to return character with 16th smallest ASCII value among those
    characters in the string that occur between indices 46 to 82, both inclusive."""
    ascii_sort = sorted([ch for ch in s[46:83]], key=lambda ch: ord(ch))
    if len(ascii_sort) < 16:
        return None
    else:
        return ascii_sort[15]