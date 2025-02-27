def return_nth_smallest_ascii(s):
    sub = s[10:83]
    asc = [ord(c) for c in sub]
    asc.sort()
    return chr(asc[17])