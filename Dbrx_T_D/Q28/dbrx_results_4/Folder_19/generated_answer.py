def return_nth_smallest_ascii(s):
    ascii_list = sorted((ord(c) for c in s if 0 <= s.index(c) <= 18))
    return chr(ascii_list[12]) if len(ascii_list) > 13 else None