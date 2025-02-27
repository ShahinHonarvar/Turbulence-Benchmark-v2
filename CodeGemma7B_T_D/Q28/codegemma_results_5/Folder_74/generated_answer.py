def return_nth_smallest_ascii(itr):
    ascii_list = sorted([ord(i) for i in itr])
    return chr(ascii_list[5]) if len(ascii_list) >= 6 else None