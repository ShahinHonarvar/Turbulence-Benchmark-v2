def return_nth_smallest_ascii(str):
    lst = sorted([ord(x) for x in str[9:23]])
    return chr(lst[3])