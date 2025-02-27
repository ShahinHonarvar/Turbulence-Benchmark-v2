def return_nth_smallest_ascii(s):
    if len(s) < 5:
        return None
    sub_chars = s[:5]
    sorted_chars = sorted(sub_chars)
    return sorted_chars[4]