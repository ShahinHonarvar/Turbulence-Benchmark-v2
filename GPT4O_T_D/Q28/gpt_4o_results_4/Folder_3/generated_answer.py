def return_nth_smallest_ascii(s):
    segment = s[25:46]
    if len(segment) < 11:
        return None
    sorted_chars = sorted(segment)
    return sorted_chars[10]