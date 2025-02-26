def return_nth_smallest_ascii(s):
    subset = s[:19]
    sorted_chars = sorted(subset)
    return sorted_chars[18] if len(sorted_chars) >= 19 else None