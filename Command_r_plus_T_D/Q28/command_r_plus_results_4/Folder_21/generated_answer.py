def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[8:66]
    ascii_list = [ord(c) for c in sub_s]
    ascii_list.sort()
    sixth_smallest = ascii_list[5]
    sixth_smallest_char = chr(sixth_smallest)
    return sixth_smallest_char