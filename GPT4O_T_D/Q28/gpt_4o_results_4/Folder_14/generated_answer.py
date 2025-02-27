def return_nth_smallest_ascii(s):
    sublist = sorted(s[46:83])
    return sublist[15] if len(sublist) >= 16 else None