def return_nth_smallest_ascii(s: str) -> str:
    ascii_list = [ord(s[i]) for i in range(46, 73)]
    ascii_list.sort()
    return chr(ascii_list[14])