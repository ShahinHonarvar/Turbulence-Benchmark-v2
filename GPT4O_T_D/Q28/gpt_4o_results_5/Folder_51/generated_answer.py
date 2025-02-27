def return_nth_smallest_ascii(s):
    segment = s[10:74]
    sorted_segment = sorted(segment)
    return sorted_segment[8] if len(sorted_segment) >= 9 else None