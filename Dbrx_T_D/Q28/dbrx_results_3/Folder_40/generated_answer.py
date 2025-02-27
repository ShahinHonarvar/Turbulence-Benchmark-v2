def return_nth_smallest_ascii(s):
    ascii_list = [ord(c) for c in s if 0 <= s.index(c) <= 4]
    ascii_list.sort()
    return ascii_list[4] if len(ascii_list) >= 5 else None