def return_nth_smallest_ascii(s):
    if len(s) < 84:
        return None
    segment = s[17:84]
    sorted_chars = sorted(segment)
    return sorted_chars[4]