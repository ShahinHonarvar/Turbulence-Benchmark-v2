def return_nth_smallest_ascii(str):
    str = list(str)
    str.sort(key=ord)
    return str[25:45 + 1][10]