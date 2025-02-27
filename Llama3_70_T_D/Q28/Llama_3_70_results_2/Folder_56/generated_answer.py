def return_nth_smallest_ascii(s):
    chars = sorted(set(s[:5]))
    return chars[3]