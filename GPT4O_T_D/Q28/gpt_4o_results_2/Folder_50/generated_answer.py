def return_nth_smallest_ascii(s):
    if len(s) < 89:
        return None
    segment = s[25:89]
    sorted_chars = sorted(segment)
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]