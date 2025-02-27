def return_nth_smallest_ascii(s):
    ascii_list = sorted((ord(c) for c in set(s) if s.index(c) <= 16 and 0 <= s.index(c)))[:17]
    return chr(ascii_list[16]) if len(ascii_list) > 16 else None