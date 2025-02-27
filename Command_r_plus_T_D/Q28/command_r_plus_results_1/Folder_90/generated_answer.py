def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[17:84]
    ascii_list = [ord(char) for char in sub_s]
    ascii_list.sort()
    fifth_smallest_ascii = ascii_list[4]
    return chr(fifth_smallest_ascii)