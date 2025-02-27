def return_nth_smallest_ascii(s):
    if len(s) < 6:
        return None
    segment = s[:6]
    sorted_segment = sorted(segment)
    return sorted_segment[5]