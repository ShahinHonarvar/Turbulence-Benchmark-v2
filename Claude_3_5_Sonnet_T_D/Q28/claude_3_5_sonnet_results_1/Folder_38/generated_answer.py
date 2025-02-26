def return_nth_smallest_ascii(s):
    valid_chars = s[:46]
    sorted_chars = sorted(valid_chars)
    if len(sorted_chars) >= 10:
        return sorted_chars[9]
    else:
        return None