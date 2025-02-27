def return_nth_smallest_ascii(s):
    if len(s) < 66:
        return None
    segment = s[17:66]
    if len(segment) < 8:
        return None
    sorted_chars = sorted(segment, key=ord)
    return sorted_chars[7]