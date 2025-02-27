def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[10:74]
    ascii_list = [ord(c) for c in sub_s]
    ascii_list.sort()
    ninth_smallest = ascii_list[8]
    return chr(ninth_smallest)