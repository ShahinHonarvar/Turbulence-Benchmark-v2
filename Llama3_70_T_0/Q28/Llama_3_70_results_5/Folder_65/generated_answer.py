def return_nth_smallest_ascii(s):
    s = ''.join(sorted([c for c in s if 32 <= ord(c) <= 67]))
    return s[11]