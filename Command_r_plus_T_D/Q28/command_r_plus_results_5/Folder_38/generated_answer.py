def return_nth_smallest_ascii(s: str) -> str:
    ascii_list = [ord(s[i]) for i in range(min(46, len(s)))]
    ascii_list.sort()
    return chr(ascii_list[9])