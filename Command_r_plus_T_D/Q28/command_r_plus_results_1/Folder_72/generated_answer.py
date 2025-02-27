def return_nth_smallest_ascii(s: str) -> str:
    ascii_list = [ord(c) for c in s[33:61]]
    ascii_list.sort()
    return chr(ascii_list[17])