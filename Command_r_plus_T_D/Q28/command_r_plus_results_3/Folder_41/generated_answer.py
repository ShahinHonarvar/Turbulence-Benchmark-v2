def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[58:86]
    ascii_list = [ord(c) for c in sub_str]
    ascii_list.sort()
    return chr(ascii_list[18])