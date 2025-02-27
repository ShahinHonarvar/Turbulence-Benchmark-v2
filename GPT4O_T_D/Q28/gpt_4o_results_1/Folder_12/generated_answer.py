def return_nth_smallest_ascii(s):
    if len(s) < 27:
        return None
    part = s[3:27]
    ascii_sorted = sorted(part, key=lambda x: ord(x))
    return ascii_sorted[4]