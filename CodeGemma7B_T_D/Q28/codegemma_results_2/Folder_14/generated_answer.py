def return_nth_smallest_ascii(str):
    str = sorted(str, key=ord)
    return str[46:83][15]