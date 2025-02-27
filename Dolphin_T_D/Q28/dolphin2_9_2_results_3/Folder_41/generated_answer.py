def return_nth_smallest_ascii(s):
    sub = s[58:86]
    sorted_chars = sorted(set(sub), key=lambda x: ord(x))
    return sorted_chars[18]