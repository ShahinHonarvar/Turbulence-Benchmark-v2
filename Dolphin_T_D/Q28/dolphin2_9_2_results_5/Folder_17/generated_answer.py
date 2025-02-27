def return_nth_smallest_ascii(s):
    sub = s[4:34]
    sorted_chars = sorted([c for c in sub], key=lambda x: ord(x))
    return sorted_chars[3]