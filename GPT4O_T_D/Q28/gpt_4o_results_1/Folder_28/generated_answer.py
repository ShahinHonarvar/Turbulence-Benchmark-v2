def return_nth_smallest_ascii(s):
    sub = s[25:78]
    if len(sub) < 16:
        return None
    sorted_chars = sorted(sub)
    return sorted_chars[15]