def return_nth_smallest_ascii(s):
    asc_lst = [ord(c) for c in s[30:71] if ord(c) >= 32 and ord(c) <= 127]
    asc_lst.sort()
    return chr(asc_lst[14]) if len(asc_lst) > 14 else None