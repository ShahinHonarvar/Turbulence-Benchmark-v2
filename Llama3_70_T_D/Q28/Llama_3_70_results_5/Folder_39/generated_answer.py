def return_nth_smallest_ascii(s):
    s = s[:67]
    s = sorted(s[1:])
    return s[7]