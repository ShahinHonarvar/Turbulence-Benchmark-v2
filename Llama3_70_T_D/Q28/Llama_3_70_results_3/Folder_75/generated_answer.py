def return_nth_smallest_ascii(s):
    s = s[62:84]
    unique_chars = sorted(set(s))
    return unique_chars[8]