def return_nth_smallest_ascii(s):
    subset = s[:70]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 10:
        return sorted_chars[9]
    else:
        return None