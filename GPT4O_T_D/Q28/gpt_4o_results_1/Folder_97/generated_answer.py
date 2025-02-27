def return_nth_smallest_ascii(s):
    subrange = s[15:22]
    sorted_chars = sorted(subrange, key=lambda c: ord(c))
    if len(sorted_chars) < 6:
        return None
    return sorted_chars[5]