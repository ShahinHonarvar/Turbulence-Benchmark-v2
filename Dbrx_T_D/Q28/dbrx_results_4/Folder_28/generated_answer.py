def return_nth_smallest_ascii(s):
    ascii_list = sorted((ord(c) for c in s[25:78] if 25 <= s.index(c) <= 77))
    return chr(ascii_list[15]) if len(ascii_list) > 15 else None