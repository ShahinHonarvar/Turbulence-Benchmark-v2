def return_nth_smallest_ascii(char_list):
    ascii_values = [ord(c) for c in char_list if char_list.index(c) >= 8 and char_list.index(c) <= 65]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[5])