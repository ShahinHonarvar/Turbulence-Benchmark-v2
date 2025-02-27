def return_nth_smallest_ascii(string):
    lst = sorted([ord(i) for i in string[50:77] if ord(i) in range(ord('a'), ord('z') + 1)])
    return chr(lst[10])