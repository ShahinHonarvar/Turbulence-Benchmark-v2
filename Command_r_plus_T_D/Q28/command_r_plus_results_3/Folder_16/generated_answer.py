def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[18:46]
    ascii_list = [ord(char) for char in sub_s]
    ascii_list.sort()
    seventh_smallest_ascii = ascii_list[6]
    seventh_smallest_char = chr(seventh_smallest_ascii)
    return seventh_smallest_char