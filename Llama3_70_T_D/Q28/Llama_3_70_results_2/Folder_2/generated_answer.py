def return_nth_smallest_ascii(s):
    s = s[48:77]
    unique_chars = sorted(set(s))
    return unique_chars[4]