def return_nth_smallest_ascii(s):
    sorted_chars = sorted([c for c in s[0:11]])
    return sorted_chars[10]