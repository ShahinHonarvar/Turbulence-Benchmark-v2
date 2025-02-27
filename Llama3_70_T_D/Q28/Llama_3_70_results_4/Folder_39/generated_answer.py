def return_nth_smallest_ascii(s):
    s = s[1:67]
    s = ''.join(sorted(s))
    return s[7]