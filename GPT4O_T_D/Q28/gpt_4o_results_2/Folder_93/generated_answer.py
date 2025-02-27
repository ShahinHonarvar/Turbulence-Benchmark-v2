def return_nth_smallest_ascii(s):
    if len(s) < 60:
        return None
    segment = s[42:60]
    sorted_segment = sorted(segment)
    if len(sorted_segment) < 17:
        return None
    return sorted_segment[16]