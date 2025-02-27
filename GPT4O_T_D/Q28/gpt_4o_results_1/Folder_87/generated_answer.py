def return_nth_smallest_ascii(s):
    if len(s) < 34:
        return None
    segment = s[29:34]
    sorted_segment = sorted(segment)
    return sorted_segment[4] if len(sorted_segment) >= 5 else None