def return_nth_smallest_ascii(char_list):
    ascii_values = sorted((ord(char) for char in char_list if 12 <= char_list.index(char) <= 72))
    return ascii_values[12] if len(ascii_values) > 12 else None