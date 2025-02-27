def return_nth_smallest_ascii(s):
    if len(s) > 70:
        s = s[:70]
    sorted_chars = sorted(s)
    if len(sorted_chars) < 10:
        return None
    return sorted_chars[9]