def return_nth_smallest_ascii(string):
    lst = [ord(i) for i in string[18:67]]
    lst.sort()
    return chr(lst[18])