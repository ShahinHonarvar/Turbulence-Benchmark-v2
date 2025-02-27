def return_nth_smallest_ascii(char_list):
    ascii_values = [ord(c) for c in char_list if char_list.index(c) <= 6]
    ascii_values.sort()
    if len(ascii_values) >= 7:
        return chr(ascii_values[6])
    else:
        return None