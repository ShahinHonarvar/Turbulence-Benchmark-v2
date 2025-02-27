def return_nth_smallest_ascii(s):
    return sorted([c for c in s[32:61] if c.isascii()])[17]