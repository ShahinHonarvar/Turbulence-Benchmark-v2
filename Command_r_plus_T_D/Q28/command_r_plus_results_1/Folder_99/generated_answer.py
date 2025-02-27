def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[17:66]
    ascii_list = [ord(c) for c in sub_s]
    ascii_list.sort()
    return chr(ascii_list[7])