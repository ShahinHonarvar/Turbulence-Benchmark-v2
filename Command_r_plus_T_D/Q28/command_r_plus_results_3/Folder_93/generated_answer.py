def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[42:60]
    ascii_list = [ord(char) for char in sub_s]
    ascii_list.sort()
    return chr(ascii_list[16])