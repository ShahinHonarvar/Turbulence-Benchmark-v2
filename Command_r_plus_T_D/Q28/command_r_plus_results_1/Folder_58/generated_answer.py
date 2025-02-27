def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[8:27]
    ascii_list = [ord(c) for c in sub_str]
    ascii_list.sort()
    sixth_smallest = ascii_list[5]
    return chr(sixth_smallest)