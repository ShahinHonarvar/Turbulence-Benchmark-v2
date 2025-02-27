def return_nth_smallest_ascii(s):
    if len(s) < 67:
        s = s[1:]
    else:
        s = s[1:67]
    sorted_chars = sorted(s, key=lambda x: ord(x))
    return sorted_chars[7] if len(sorted_chars) >= 8 else None