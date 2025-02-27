def return_nth_smallest_ascii(s):
    return sorted([c for c in s[10:91] if ord(c)])[19]