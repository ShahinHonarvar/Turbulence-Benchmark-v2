def return_nth_smallest_ascii(str):
    str = str[63:77]
    str = sorted(str, key=ord)
    return str[13]