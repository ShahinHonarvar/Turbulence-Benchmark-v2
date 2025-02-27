def return_nth_smallest_ascii(s: str) -> str:
    ascii_list = [ord(c) for c in s if 33 <= ord(c) <= 85]
    ascii_list.sort()
    return chr(ascii_list[12]) if len(ascii_list) > 12 else ''