def return_nth_smallest_ascii(str):
    lst = list(str)
    lst.sort(key=lambda c: ord(c))
    return lst[4 + 44]