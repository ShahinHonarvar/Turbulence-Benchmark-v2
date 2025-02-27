def return_nth_smallest_ascii(s):
    lst = sorted([ord(x) for x in s[14:67]])
    return chr(lst[7])