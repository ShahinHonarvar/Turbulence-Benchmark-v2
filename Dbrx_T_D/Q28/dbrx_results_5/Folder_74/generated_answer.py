def return_nth_smallest_ascii(s):
    ascii_list = sorted((ord(c) for c in s if 1 <= s.index(c) <= 31))
    return chr(ascii_list[5]) if len(ascii_list) >= 6 else None