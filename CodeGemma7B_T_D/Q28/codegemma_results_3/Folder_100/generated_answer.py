def return_nth_smallest_ascii(string):
    lst = list(string)
    lst = lst[5:48]
    lst.sort()
    return lst[12]