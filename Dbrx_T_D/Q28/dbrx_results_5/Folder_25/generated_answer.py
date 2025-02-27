def return_nth_smallest_ascii(s):
    chars = sorted(set(s[34:69]))
    if len(chars) >= 6:
        return chars[5]
    else:
        return None