def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[47:81]
    ascii_list = [(ord(char), char) for char in sub_s]
    ascii_list.sort()
    return ascii_list[3][1]