def return_nth_smallest_ascii(s):
    lst = sorted([ord(ch) for ch in s[51:79]])
    return chr(lst[8])