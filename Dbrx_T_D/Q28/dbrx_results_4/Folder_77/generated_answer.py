def return_nth_smallest_ascii(string):
    ascii_list = sorted((ord(c) for c in string if 63 <= ord(c) <= 76))
    return chr(ascii_list[13]) if len(ascii_list) > 13 else None