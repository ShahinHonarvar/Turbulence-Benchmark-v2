def return_nth_smallest_ascii(s):
    segment = sorted(s[:14])
    return segment[13] if len(segment) > 13 else None