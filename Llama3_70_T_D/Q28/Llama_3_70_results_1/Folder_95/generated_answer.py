def return_nth_smallest_ascii(s):
    s = s[1:47]
    unique_chars = sorted(set(s))
    return unique_chars[12]