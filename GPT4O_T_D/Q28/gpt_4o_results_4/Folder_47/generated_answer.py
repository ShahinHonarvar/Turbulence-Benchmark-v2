def return_nth_smallest_ascii(s):
    sublist = [ord(s[i]) for i in range(3, min(len(s), 53))]
    sublist.sort()
    if len(sublist) < 8:
        return None
    return chr(sublist[7])