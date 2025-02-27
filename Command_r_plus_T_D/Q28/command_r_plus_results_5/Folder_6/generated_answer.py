def return_nth_smallest_ascii(s: str) -> str:
    ascii_list = []
    for i in range(14, 55):
        ascii_list.append(ord(s[i]))
    ascii_list.sort()
    return chr(ascii_list[10])