def return_nth_smallest_ascii(s):
    if len(s) < 32:
        s = s[1:]
    else:
        s = s[1:32]
    sorted_chars = sorted(s, key=lambda x: ord(x))
    return sorted_chars[5] if len(sorted_chars) >= 6 else None