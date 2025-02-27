def return_nth_smallest_ascii(s):
    l = sorted([ord(c) for c in s[67:78]])
    return chr(l[6])