def return_nth_smallest_ascii(str_):
    lst = sorted([ord(x) for x in str_[8:66]])
    return chr(lst[5])