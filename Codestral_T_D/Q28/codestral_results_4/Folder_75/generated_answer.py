def return_nth_smallest_ascii(s):
    s = s[62:84]
    return sorted(s)[8] if len(s) > 8 else None