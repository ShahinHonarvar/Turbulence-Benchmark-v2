def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[:46])
    if len(sorted_chars) < 10:
        return None
    return sorted_chars[9]