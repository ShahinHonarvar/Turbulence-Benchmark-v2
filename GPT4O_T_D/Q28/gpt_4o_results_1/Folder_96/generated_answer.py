def return_nth_smallest_ascii(s):
    if len(s) < 18:
        return None
    segment = s[:18]
    sorted_segment = sorted(segment)
    return sorted_segment[17]