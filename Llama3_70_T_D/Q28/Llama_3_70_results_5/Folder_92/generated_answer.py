def return_nth_smallest_ascii(s):
    s = ''.join(sorted(s[:4]))
    return s[3]