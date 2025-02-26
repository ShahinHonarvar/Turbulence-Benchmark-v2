def return_nth_smallest_ascii(s):
    chars = s[:70]
    sorted_chars = sorted(chars)
    if len(sorted_chars) >= 10:
        return sorted_chars[9]
    else:
        return None