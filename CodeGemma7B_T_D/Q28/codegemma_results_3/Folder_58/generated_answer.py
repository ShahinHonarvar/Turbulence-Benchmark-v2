def return_nth_smallest_ascii(s):
    li = sorted([ord(i) for i in s])[8:27]
    return chr(li[5])