def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[44:70]
    ascii_list = [ord(c) for c in sub_s]
    ascii_list.sort()
    return chr(ascii_list[14])