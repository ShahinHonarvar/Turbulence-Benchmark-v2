def return_nth_smallest_ascii(s):
    s = s[6:59]
    sorted_chars = sorted(set(s))
    return sorted_chars[18]