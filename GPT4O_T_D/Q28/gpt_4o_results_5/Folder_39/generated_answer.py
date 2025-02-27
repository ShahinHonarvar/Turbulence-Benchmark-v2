def return_nth_smallest_ascii(s):
    if len(s) < 66:
        s = s[1:]
    else:
        s = s[1:67]
    sorted_chars = sorted(s, key=ord)
    if len(sorted_chars) >= 8:
        return sorted_chars[7]
    return None