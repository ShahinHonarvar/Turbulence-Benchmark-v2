def return_nth_smallest_ascii(s: str) -> str:
    ascii_list = [ord(c) for c in s[1:47]]
    ascii_list.sort()
    return chr(ascii_list[12])