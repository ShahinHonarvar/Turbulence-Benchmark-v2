def return_nth_smallest_ascii(s):
    ascii_list = sorted((ord(c) for c in set(s[14:67])))
    return chr(ascii_list[7]) if len(ascii_list) > 7 else None