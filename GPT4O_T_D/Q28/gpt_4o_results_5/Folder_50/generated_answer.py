def return_nth_smallest_ascii(s):
    segment = s[25:89]
    if len(segment) < 11:
        return None
    sorted_segment = sorted(segment)
    return sorted_segment[10] if len(sorted_segment) > 10 else None