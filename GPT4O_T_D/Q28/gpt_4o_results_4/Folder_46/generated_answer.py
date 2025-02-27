def return_nth_smallest_ascii(s):
    if len(s) < 86:
        return None
    segment = s[34:86]
    sorted_segment = sorted(segment)
    return sorted_segment[19] if len(sorted_segment) >= 20 else None