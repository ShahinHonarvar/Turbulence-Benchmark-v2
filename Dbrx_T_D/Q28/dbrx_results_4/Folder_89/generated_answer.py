def return_nth_smallest_ascii(char_list):
    ascii_values = [ord(char) for char in char_list[24:72] if char.isascii() and 24 <= char_list.index(char) <= 71]
    sorted_ascii_values = sorted(ascii_values)[:8]
    return chr(sorted_ascii_values[7])