def return_nth_smallest_ascii(str):
    str = str[5:48]
    str = sorted(str, key=lambda char: ord(char))
    return str[12]