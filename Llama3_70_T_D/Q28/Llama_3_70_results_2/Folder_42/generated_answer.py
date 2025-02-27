def return_nth_smallest_ascii(s):
    s = s[12:73]
    distinct_chars = sorted(set(s))
    return distinct_chars[12]