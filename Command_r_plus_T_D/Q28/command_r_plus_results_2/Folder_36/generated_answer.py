def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[17:57]
    ascii_list = [ord(char) for char in sub_s]
    ascii_list.sort()
    ninth_smallest_ascii = ascii_list[8]
    ninth_smallest_char = chr(ninth_smallest_ascii)
    return ninth_smallest_char