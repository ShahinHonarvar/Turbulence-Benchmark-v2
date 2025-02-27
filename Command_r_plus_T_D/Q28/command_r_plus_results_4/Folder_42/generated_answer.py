def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[12:73]
    ascii_list = [ord(char) for char in sub_str]
    ascii_list.sort()
    return chr(ascii_list[12])